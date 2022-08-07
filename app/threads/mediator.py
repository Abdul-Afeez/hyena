import time

from app.consts.const import RAN, PENDING, FAILED, QUEUED, RUNNING, QUILL_URL, TECH_POINT_URL, \
    PARAPHRASING_MISMATCH_ERROR
from app.models.base import Job
from app.tools.browser import Browser
from app.tools.quill_engine import Quill
from app.websites.blogger import Blogger
from app.websites.disrupt_africa.disrupt_africa import DisruptAfricaParser
from app.websites.scanner import Scanner
from app.websites.techpoint.techpoint_browser import Spider
from app.websites.techpoint.techpointparser import TechPointParser


class Scheduler:
    rules = [
        # {'link': QUILL_URL, 'max_session': 1, 'delay': 3},
        {'link': TECH_POINT_URL, 'max_session': 4, 'delay': 3},
    ]

    def __init__(self):
        # Delete Quill jobs
        Job.delete().where((Job.url == QUILL_URL & Job.sub_status != PARAPHRASING_MISMATCH_ERROR) & (
                (Job.status == RUNNING) | (Job.status == RAN))).execute()

        # Delete old running jobs
        Job.delete().where(Job.status == RUNNING).execute()

        pending_or_queued_quill_job = Job.filter(
            (Job.url == QUILL_URL) & ((Job.status == PENDING) | (Job.status == QUEUED)))
        if not pending_or_queued_quill_job:
            pass
            # Thread.queue_job(QUILL_URL, QUILL_URL, {'url': QUILL_URL, 'opener': True})
        self.pending_jobs = []

    def get_pending_jobs(self):
        for index, rule in enumerate(Scheduler.rules):
            link = rule.get("link")
            max_session = rule.get("max_session")
            # print(f'Scheduler running for {link}.....................')
            next_run = rule.get('next_run', None)
            delay = rule.get('delay', 1)
            now = round(time.time())
            pending_or_running_jobs = Job.filter(
                (Job.link == link) & ((Job.status == PENDING) | (Job.status == RUNNING)))
            if not next_run:
                new_next_run = now + delay * 60
                # print(f'Setting next run time to {new_next_run}')
                Scheduler.rules[index] = {**Scheduler.rules[index], 'next_run': new_next_run}
            elif now < next_run and len(pending_or_running_jobs):
                # print(f'Delaying  because next_run {next_run} is < now {now} ')
                continue
            # print(f'pending_or_running_jobs == {len(pending_or_running_jobs)}')
            difference = max_session - len(pending_or_running_jobs)
            # print(f'max_session == {max_session}, difference == {difference}')
            if difference >= 1:
                queued_jobs = Job.filter(status=QUEUED, link=link)
                # print(f'Discovered {len(queued_jobs)} queued jobs on link {link}')
                for que_index, queued_job in enumerate(queued_jobs):
                    if que_index == max_session:
                        break
                    queued_job.status = PENDING
                    queued_job.save()
            else:
                # print('More jobs are sufficiently running for now')
                pass

        # print('Sleeping till jobs arrive')
        time.sleep(5)
        self.pending_jobs = Job.filter(status=PENDING)
        return self.pending_jobs


class Mediator:
    threads = {}
    browser = None

    def __init__(self):
        Mediator.browser = Browser()
        Mediator.browser.get_driver()
        self.thread_factory = ThreadFactory()

    def run(self):
        scheduler = Scheduler()
        while True:
            pending_jobs = scheduler.get_pending_jobs()
            for job in pending_jobs:
                # print(job.meta)
                print(f'Enqueuing job with url === {job.url}')
                self.enqueue_thread(job)
                # print(f'Enqueued job with url === {job.url} successfully')
            # print(f'Browser History = {Browser.history}')
            last_memory = None
            for url in Browser.history:
                if last_memory and last_memory == url:
                    pass
                else:
                    Mediator.browser.switch_to_tab(url)
                # print(f'Getting thread for url === {url}')
                thread = Mediator.threads.get(url, None)
                if thread:
                    # print(f'Executing thread for url === {url}')
                    thread.execute()
                    # print(f'Thread Execution for url === {url} completed')
                    last_memory = url

    def handle_thread(self, thread):
        pass

    def enqueue_thread(self, job):
        # try:
        print(f'Registering {job.id} on {job.url}')
        self.thread_factory.register_thread(job)
        # except Exception as e:
        #     # print(e)

    @staticmethod
    def terminate(url):
        try:
            previous_tab_index = 0
            history_length = len(Mediator.browser.history)
            if history_length == 1:
                Browser.session_id = None
            else:
                previous_tab_index = Mediator.browser.history.index(url) - 1
            print(f'Removing {url} from {Mediator.threads}')

            del Mediator.threads[url]
            Mediator.browser.close_tab(url)
            print('Switching browser to previous tab')
            Mediator.browser.switch_to_tab(Mediator.browser.history[previous_tab_index])
        except Exception as e:
            print(e)
            pass


class Thread:
    PENDING = 'PENDING'
    RUNNING = 'RUNNING'
    RAN = 'RAN'

    def __init__(self, job):
        self.browser = Mediator.browser
        self.driver = Mediator.browser.driver
        self.job = job
        self.payload = job.meta
        self.steps = []
        self.exit_on_complete = True

    def get_now(self):
        return round(time.time())

    def release(self):
        # self.job.status = PENDING
        # self.job.save()
        print(f'Releasing after self.job.id == {self.job.id}, self.job.status == {self.job.status}')
        steps = self.steps
        for index, step in enumerate(steps):
            if index == 0:
                steps[index] = {**step, 'max_health_check': 40, 'started_at': None, 'status': Thread.RAN, 'retries': 4}
                self.steps = steps
            else:
                steps[index] = {**step, 'max_health_check': 40, 'started_at': None, 'status': Thread.PENDING,
                                'retries': 4}
                self.steps = steps
        print(self.steps)

    def set_job(self, job):
        self.job = job
        self.payload = job.meta

    @staticmethod
    def queue_job(link, url, data):
        job = Job()
        job.url = url
        job.meta = data
        job.link = link
        # print(f'Saving {url}')
        job.status = QUEUED
        job.save()

    def execute(self):
        # print('Executing......................')
        steps = self.steps
        for index, step in enumerate(steps):
            print(self.job.id, self.job.url, self.job.status)
            print(step)
            # print(f'Can I Execute...................... {index} self.job.status == {self.job.status}')
            status = step.get('status', Thread.PENDING)
            timeout = step.get('timeout', 0) * 60
            retries = step.get('retries', 3)
            now = self.get_now()
            started_at = step.get('started_at', now) or now
            url = self.payload.get('url', None)
            steps[index] = {**steps[index], 'last_updated': now}
            self.steps = steps
            execution_time = (now - started_at)
            timed_out = execution_time >= timeout
            if not retries or (self.job.status == RUNNING and timed_out):
                print('Timed out')
                self.job.status = FAILED if retries else 'TIMEOUT'
                self.job.meta = {**self.job.meta, 'retries': retries, 'execution_time': execution_time,
                                 'timed_out': timed_out}
                self.job.save()
                self.release()
                if self.exit_on_complete:
                    Mediator.terminate(url)
                break
            if status == Thread.PENDING and self.job.status in [PENDING, RUNNING]:
                # print(f'Executing...................... {index}')
                # print(f'Started running step {index + 1} of {len(self.steps)} steps under url === {url} ')
                try:
                    step.get('method')()
                    # print(f'Changing step {step.get("method")} to RUNNING')
                    self.job.status = Thread.RUNNING
                    self.job.save()
                    steps[index] = {**steps[index], 'status': Thread.RUNNING, 'started_at': started_at}
                    self.steps = steps
                except Exception as e:
                    print('Encountered error while running')
                    print(e)
                    steps[index] = {**steps[index], 'status': Thread.PENDING,
                                    'retries': retries - 1}
                    self.steps = steps
                    # self.browser.driver.save_screenshot(f'{self.job.meta.get("url")}-error-retries{retries - 1}.png')
                    # print(e)
                # print(f'Ended running step {index + 1} of {len(self.steps)} steps under url === {url}')
                break
            elif status == Thread.RUNNING and self.job.status in [RUNNING]:
                print(f'Checking if step is healthy')
                self.steps = steps
                max_health_check = step.get('max_health_check', 0)
                sleep = step.get('sleep', 0)
                # sleep for specified amount of time so that max time per step == timeout * max_health_check
                time.sleep(sleep)
                health_check = step.get('method')(health_check=True)
                print(f'Healthcheck returned {health_check}')
                if health_check:
                    print('health_check and setting thread status to RAN')  # WIP, please wait and check back later
                    steps[index] = {**steps[index], 'status': Thread.RAN}
                elif max_health_check:
                    print('Using max_health_check potion to retry')  # WIP, please wait and check back later
                    steps[index] = {**steps[index], 'max_health_check': max_health_check - 1}
                else:
                    print(f'Terminating {health_check} for no reason I guess')
                    Mediator.terminate(url)
                break
            elif (status == Thread.RAN) and (index == len(self.steps) - 1) and self.exit_on_complete:
                print(f'Terminating due to exit_on_complete')
                self.job.status = RAN
                self.job.save()
                Mediator.terminate(url)
                break
            elif (status == Thread.RAN) and (index == len(self.steps) - 1):
                # print('Releasing Thread')
                self.job.status = RAN
                self.job.save()
                self.release()
                break
            else:
                # print('Cant re run a completed thread that has been released would rather wait')
                continue


class ThreadFactory:

    def __int__(self):
        pass

    def register_thread(self, job):
        url = job.url
        print(f'url === {url}  and Mediator.threads === {Mediator.threads}')
        if url in Mediator.threads.keys():
            # print(f'Using Existing Thread Runner for new f{job.id}')
            existing_thread = Mediator.threads.get(url)
            existing_thread.set_job(job)
            return existing_thread

        if url == TECH_POINT_URL:
            new_thread = ReconnaissanceThread(job)
        elif TECH_POINT_URL in url:
            new_thread = ParserThread(job, TechPointParser)
        elif 'https://disrupt-africa.com' in url:
            new_thread = ParserThread(job, DisruptAfricaParser)
        elif url == QUILL_URL:
            new_thread = QuillThread(job)
        else:
            new_thread = Thread(job)
        if new_thread:
            try:
                if not len(Mediator.browser.history):
                    # print('Mediator.browser.driver.get(url)')
                    Mediator.browser.get(url)
                else:
                    # print('Mediator.browser.open_link_in_new_tab(url)')
                    Mediator.browser.open_link_in_new_tab(url)
                Mediator.threads[url] = new_thread
            except Exception as e:
                # print(e)
                pass
            return new_thread
        else:
            raise Exception('Cant open the thread')


class QuillThread(Thread):
    PROCESS_REFRESH_LIMIT = 2

    def __init__(self, job):
        super().__init__(job)
        self.quill = Quill()
        self.process_refresh_limit = QuillThread.PROCESS_REFRESH_LIMIT
        self.blogger = None
        self.exit_on_complete = False
        self.steps = [
            {'method': self.step_1, 'retries': 4,
             'timeout': 20, 'max_health_check': 40, 'sleep': 0},
            {'method': self.step_2, 'retries': 4,
             'timeout': 20, 'max_health_check': 40, 'sleep': 0},
            {'method': self.step_3, 'retries': 4,
             'timeout': 20, 'max_health_check': 40, 'sleep': 0},
            {'method': self.step_4, 'retries': 4,
             'timeout': 20, 'max_health_check': 40, 'sleep': 0}
        ]

    def step_1(self, health_check=False):
        # login to quill
        if health_check:
            return True
        else:
            self.quill.set_browser(self.browser)
            self.quill.authenticate()

    def step_2(self, health_check=False):
        if health_check:
            return True
        else:
            self.process_refresh_limit -= 1
            if self.process_refresh_limit < 0:
                self.process_refresh_limit = QuillThread.PROCESS_REFRESH_LIMIT
                self.quill.refresh_browser()
            blogger = Blogger()
            blogger.set_state(self.payload)
            self.blogger = blogger
            c_input = blogger.get_rephrase_text()
            paraphrased_text = self.job.meta.get('paraphrased_text', None)
            if self.payload.get('opener', False) or (
                    self.job.status not in [PENDING, RUNNING]):  # FAILED OR QUEUED along
                steps = self.steps
                steps[2] = {**self.steps[2], 'status': RAN}
                steps[3] = {**self.steps[3],
                            'status': RAN}  # So that the other QUEUED can go to PENDING from the step 3 health check
                self.steps = steps
            if paraphrased_text:  # Already paraphrased but failed earlier, now been retried by changing status to PENDING with old data
                steps = self.steps
                steps[2] = {**self.steps[2], 'status': RAN}
                self.steps = steps
            else:
                self.job.meta['c_input'] = c_input
                self.job.save()
                self.quill.set_text(c_input)

    def step_3(self, health_check=False):
        # return True
        if health_check:
            return Quill.wait()
        else:
            self.quill.click_paraphrase_button()

    def step_4(self, health_check=False):
        # return True
        if health_check:
            return True
        else:
            paraphrased_text = self.job.meta.get('paraphrased_text', None)
            if not paraphrased_text:
                paraphrased_text = self.quill.copy()
            self.blogger.save_local_content(paraphrased_text, '-output-1-raw')
            self.blogger.save_local_content(paraphrased_text.replace('\n\n\n', '\n'), '-output-1')
            try:
                self.blogger.remove_stamp_from_tag_map(paraphrased_text)
                self.blogger.identify_keyword()
                self.blogger.post.template = self.blogger.html_to_text
                self.blogger.send_post()
                self.job.meta = {}
                self.job.sub_status = ''
                self.job.save()
            except Exception as e:
                self.job.sub_status = PARAPHRASING_MISMATCH_ERROR
                self.job.meta['paraphrased_text'] = paraphrased_text
                self.job.save()
                # print(e)


config = [
    {
        'base_url': 'https://techpoint.africa/',
        'target_links': 100,
        'url': 'https://techpoint.africa/',
        'read_more_text': "Read More",
        'href_regex': 'href="/20(.+?)">',
        'exclude_hrefs': ['digest', 'podcast'],
        'url_pattern': '{base_url}20{link}',
        'endpoint': 'https://techvented.com/api/save-article'
    },
    {
        'base_url': 'https://techcabal.com/',
        'target_links': 100,
        'url': 'https://techcabal.com/category/features/',
        'read_more_text': "See More Articles",
        'href_regex': 'href="https://techcabal.com/20(.+?)/">',
        'exclude_hrefs': [],
        'url_pattern': '{base_url}20{link}/',
        'endpoint': 'https://techvented.com/api/save-article',
    },
    {
        'base_url': 'https://disrupt-africa.com/',
        'target_links': 100,
        'url': 'https://disrupt-africa.com/category/region/east-africa/page/{page}/',
        'read_more_text': "1-300",
        'href_regex': 'href="https://disrupt-africa.com/20(.+?)/">',
        'exclude_hrefs': [],
        'url_pattern': '{base_url}20{link}/',
        'endpoint': 'https://techvented.com/api/save-article',
    }
]


class ReconnaissanceThread(Thread):
    def __init__(self, job):
        super().__init__(job)
        self.exit_on_complete = False
        self.config = config[2]
        self.spider = Spider(self.config)
        self.steps = [
            {'method': self.step_1, 'retries': 4,
             'timeout': 600, 'max_health_check': 40, 'sleep': 0},
            {'method': self.step_2, 'retries': 4,
             'timeout': 600, 'max_health_check': 40, 'sleep': 0},
            {'method': self.step_3, 'retries': 4,
             'timeout': 600, 'max_health_check': 40, 'sleep': 0}
        ]
        self.maximum = job.meta.get('maximum', 5)

    def release(self):
        super().release()  # reverse the thread to PENDING
        below_last_page = self.spider.first_page and (self.spider.current_page <= self.spider.last_page)
        if len(self.spider.urls) <= self.config.get('target_links') or below_last_page:
            self.job.status = 'RUNNING'  # Keep the main job running
            self.job.save()

    def step_1(self, health_check=False):
        if health_check:
            return True
        else:
            self.spider.set_browser(self.browser)

    def step_2(self, health_check=False):
        if health_check:
            return self.spider.get_read_more_button()
        else:
            self.spider.click_next_page()

    def step_3(self, health_check=False):
        if health_check:
            return True
        else:
            self.spider.get_page_content()
            self.spider.crawl()


class ParserThread(Thread):

    def __init__(self, job, parser):
        super().__init__(job)
        self.exit_on_complete = True
        self.blogger = parser()
        self.spider = Scanner()
        self.spider.set_browser(self.browser)
        self.html = None
        self.steps = [
            {'method': self.step_1, 'retries': 4,
             'timeout': 60, 'max_health_check': 40, 'sleep': 5}
        ]

    def step_1(self, health_check=False):
        if health_check:
            return True
        else:
            url = self.payload.get('url')
            try:
                self.html = self.spider.get_page_content()
                data = self.blogger.extract(url, self.html)
                if data:
                    Thread.queue_job(QUILL_URL, QUILL_URL, data)
            except Exception as e:
                self.browser.driver.get(url)
                raise Exception(e)
