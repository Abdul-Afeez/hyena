import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from app.websites.spider import Spider
from app.websites.validate_url import ValidateUrl

server = "https://techvented.com"


class TechPointBrowser(Spider):
    def get_url(self):
        return 'https://techpoint.africa/'

    def crawl(self, maximum):
        links = self.get_page_content()
        while len(self.urls) < maximum:
            while len(links):
                link = links.pop()
                reformed_link = f'{self.get_url()}20{link}'
                if self.cache.get(link, False) or 'podcast' in link \
                        or 'digest' in link \
                        or link in self.urls \
                        or self.double_confirm_page_crawled(reformed_link, 'http://localhost'):
                    self.cache[link] = True
                    continue
                if len(self.urls) == maximum:
                    break
                if len(self.urls) in [50, 100, 150, 200]:
                    self.save_content(self.urls, '-techpoint-urls', 'tech-point-urls')
                self.urls.append(reformed_link)
                self.urls = list(set(self.urls))
                print(f'Crawling length == {len(self.urls)}')
            links = self.click_next_page()
        print(self.urls)
        return self.urls

    def get_page_content(self):
        hrefs = re.findall('href="/20(.+?)">', str(super().get_page_content()))
        return hrefs

    def get_read_more_button(self):
        read_more_btn = None
        while not read_more_btn:
            print('Finding read_more_btn done')
            try:
                read_more = '//button[text()="Read More"]'
                read_more_btn = self.browser.find_element(By.XPATH, read_more)
            except Exception as e:
                print(e)

            time.sleep(2)
        return read_more_btn

    def click_next_page(self):
        print('click_next_page Waiting for content to load')
        read_more_btn = self.get_read_more_button()
        print('Content loaded clicking button')
        read_more_btn.click()
        self.get_read_more_button()
        return self.get_page_content()
