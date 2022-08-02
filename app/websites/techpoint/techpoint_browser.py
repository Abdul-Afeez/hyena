import re
from selenium.webdriver.common.by import By

from app.consts.const import QUEUED, TECH_POINT_URL
from app.models.base import Job
from app.websites.spider import Spider


class TechPointBrowser(Spider):
    
    def __init__(self):
        super().__init__()
        self.links = []
    
    def get_url(self):
        return TECH_POINT_URL

    def crawl(self):
        while len(self.links):
            link = self.links.pop()
            reformed_link = f'{self.get_url()}20{link}'
            if self.invalid_cache.get(link, False) or self.valid_cache.get(link, False) or 'podcast' in link \
                    or 'digest' in link \
                    or link in self.urls:
                self.invalid_cache[link] = True
                continue
            elif self.confirm_page_crawled(reformed_link):
                self.invalid_cache[link] = True
                continue
            valid_links = len(self.urls)
            if not valid_links % 10:
                self.save_content(self.urls, '-techpoint-urls', 'tech-point-urls')
            self.urls.append(reformed_link)
            try:
                job = Job()
                job.url = reformed_link
                job.meta = {'url': reformed_link}
                job.link = TECH_POINT_URL
                print(f'Saving {reformed_link}')
                job.status = QUEUED
                job.save()
            except Exception as e:
                print(e)
            self.valid_cache[reformed_link] = True
            self.urls = list(set(self.urls))
            print(f'Crawling length == {len(self.urls)}')

    def get_page_content(self):
        hrefs = re.findall('href="/20(.+?)">', str(super().get_page_content()))
        self.links = hrefs
        return hrefs

    def get_read_more_button(self):
        print('Finding read_more_btn done')
        try:
            read_more = '//button[text()="Read More"]'
            read_more_btn = self.browser.driver.find_element(By.XPATH, read_more)
            if read_more_btn:
                return read_more_btn
        except Exception as e:
            print(e)
        return False

    def click_next_page(self):
        print('click_next_page Waiting for content to load')
        read_more_btn = self.get_read_more_button()
        print('Content loaded clicking button')
        read_more_btn.click()
