import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from app.websites.validate_url import ValidateUrl

server = "https://techvented.com"


class Spider(ValidateUrl):
    browser = None

    def __init__(self):
        self.output = []
        self.urls = []
        self.url = None
        self.cache = {}

    def set_browser(self, url):
        self.url = url
        if not self.browser:
            try:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
                chrome_options.headless = True
                chrome_options.add_argument('--headless')

                self.browser = webdriver.Chrome(executable_path="app/tools/drivers/chromedriver",
                                                            options=chrome_options)
                time.sleep(6)

            except Exception as e:
                print(e)
        self.browser.get(self.url)

    def get_page_content(self):
        print('get_page_content waiting for content to load')
        time.sleep(3)
        print('Content loaded')
        body = self.browser.find_element(By.XPATH, "//html").get_attribute('innerHTML')
        print('Body copied')
        self.save_content(body, '-last-body', 'tech-point-urls')
        return body


