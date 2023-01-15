import time
from selenium.webdriver.common.by import By

from app.tools.validate_url import ValidateUrl

server = "https://techvented.com"


class Scanner(ValidateUrl):
    browser = None
    driver = None

    def __init__(self):
        from app.threads.mediator import Printer
        self.output = []
        self.urls = []
        self.url = None
        self.invalid_cache = {}
        self.valid_cache = {}
        self.printer = Printer

    def set_browser(self, browser):
        Scanner.browser = browser
        Scanner.driver = browser.driver

    def get_page_content(self):
        self.printer.basic_print('get_page_content waiting for content to load')
        time.sleep(3)
        self.printer.basic_print('Content loaded')
        html = self.driver.find_element(By.XPATH, "//html").get_attribute('innerHTML')
        self.printer.basic_print('Body copied')
        # self.save_content(body, '-last-body', 'tech-point-urls')
        # Spider.browser.quit()
        return html
