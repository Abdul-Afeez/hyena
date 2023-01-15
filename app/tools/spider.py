import re

from app.consts.const import QUEUED
from app.models.base import Job
from app.tools.scanner import Scanner


class Spider(Scanner):

    def __init__(self, web_master):
        super().__init__()
        self.first_page = 0
        self.current_page = 0
        self.last_page = 0
        self.web_master = web_master
        self.config = web_master.reconnaissance
        self.links = []
        self.detect_pagination()

    def detect_pagination(self):
        pages = self.config.get('read_more_text', '').split('-')
        if len(pages) == 2:
            self.first_page = int(pages[0])
            self.last_page = int(pages[1])

    def crawl(self):
        while len(self.links):
            link = self.links.pop()
            base_url = self.config.get('base_url')
            url_pattern = self.config.get('url_pattern')
            exclude_hrefs = self.config.get('exclude_hrefs')
            href_regex_tester = self.config.get('href_regex_tester', '')
            reformed_link = url_pattern.replace('{base_url}', base_url).replace('{link}', link)
            to_be_continued = False
            for href in exclude_hrefs:
                if href in link:
                    to_be_continued = True
                    break
            if to_be_continued or self.invalid_cache.get(link, False) or self.valid_cache.get(link,
                                                                                              False) or link in self.urls:
                self.invalid_cache[link] = True
                continue
            elif self.confirm_page_crawled(reformed_link) and (not re.search(href_regex_tester, reformed_link)):
                self.invalid_cache[link] = True
                continue
            self.urls.append(reformed_link)
            try:
                job = Job()
                job.url = reformed_link
                job.web_master_id = self.web_master.id
                job.meta = {'url': reformed_link, 'endpoint': self.config.get('endpoint')}
                # job.link = base_url
                print(f'Saving {reformed_link}')
                job.status = QUEUED
                job.save()
            except Exception as e:
                print(e)
            self.valid_cache[reformed_link] = True
            self.urls = list(set(self.urls))
            self.printer.basic_print(f'Crawling length == {len(self.urls)}')

    def get_page_content(self):
        self.printer.basic_print(str(super().get_page_content()))
        hrefs = re.findall(self.config.get('href_regex'), str(super().get_page_content()))
        self.links = hrefs
        return hrefs

    def find_or_click_read_more(self, find=True):
        read_more_text = self.config.get('read_more_text')
        possible_tags = ['a', 'button']
        read_more_btn = None
        for possible_tag in possible_tags:
            if read_more_btn:
                break
            try:
                script = f"Array.from(document.getElementsByTagName('{possible_tag}')).filter(item => item.innerText === '{read_more_text}')[0]"
                self.printer.basic_print(script)
                if find:
                    self.browser.driver \
                        .execute_script(f'{script}.innerText')
                    read_more_btn = True
                    # print(read_more_btn)
                else:
                    self.browser.driver \
                        .execute_script(f'{script}.click()')
                    read_more_btn = True
                    print(read_more_btn)
            except Exception as e:
                # print(e)
                read_more_btn = None

        return read_more_btn

    def get_read_more_button(self):
        self.printer.basic_print('Finding read_more_btn done')
        if self.first_page:
            return True
        try:
            read_more_btn = self.find_or_click_read_more(True)
            if read_more_btn:
                return read_more_btn
        except Exception as e:
            print(e)
        return False

    def click_next_page(self):
        self.printer.basic_print('click_next_page Waiting for content to load')
        self.printer.basic_print('Content loaded clicking button')
        if self.first_page:
            self.current_page += 1
            self.driver.get(self.config.get('url').replace('{page}', str(self.current_page)))
            return
        self.find_or_click_read_more(False)
