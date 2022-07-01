import re
import time
from selenium.webdriver.common.by import By

from app.websites.validate_url import ValidateUrl

server = "https://techvented.com"


class Spider(ValidateUrl):
    browser = None
    driver = None

    def __init__(self):
        self.output = []
        self.urls = []
        self.url = None
        self.invalid_cache = {}
        self.valid_cache = {}

    def set_browser(self, browser):
        Spider.browser = browser
        Spider.driver = browser.driver

    def get_page_content(self):
        print('get_page_content waiting for content to load')
        time.sleep(3)
        print('Content loaded')
        body = self.driver.find_element(By.XPATH, "//html").get_attribute('innerHTML')
        print('Body copied')
        self.save_content(body, '-last-body', 'tech-point-urls')
        # Spider.browser.quit()
        return body
