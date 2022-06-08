import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TechPointBrowser:
    browser = None
    def __init__(self):
        self.output = []
        
    def set_browser(self, url):
        if not TechPointBrowser.browser:
            try:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.headless = False
                TechPointBrowser.browser = webdriver.Chrome(executable_path="./drivers/chromedriver", options=chrome_options)
                TechPointBrowser.browser.get(url)
                time.sleep(6)

            except:
                pass

    def get_page_content(self):
        print('get_page_content waiting for content to load')
        time.sleep(3)
        print('Content loaded')
        body = TechPointBrowser.browser.find_element(By.XPATH, "//body").get_attribute('innerHTML')
        print('Body copied')
        hrefs = re.findall('href="/20(.+?)">', str(body))
        return hrefs

    def click_next_page(self):
        print('click_next_page Waiting for content to load')
        time.sleep(10)
        print('Content loaded clicking button')
        read_more = '//button[text()="Read More"]'
        read_more_btn = TechPointBrowser.browser.find_element(By.XPATH, read_more)
        print('Clicking read_more_btn done')
        time.sleep(2)
        read_more_btn.click()
        time.sleep(6)
        return self.get_page_content()
