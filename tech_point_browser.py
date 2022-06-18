# import re
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import requests
# import json
#
#
# server = "https://techvented.com"
#
#
# class TechPointBrowser:
#     browser = None
#     def __init__(self):
#         self.output = []
#         self.urls = []
#
#     def set_browser(self, url):
#         if not TechPointBrowser.browser:
#             try:
#                 chrome_options = webdriver.ChromeOptions()
#                 chrome_options.headless = False
#                 TechPointBrowser.browser = webdriver.Chrome(executable_path="./drivers/chromedriver", options=chrome_options)
#                 TechPointBrowser.browser.get(url)
#                 time.sleep(6)
#
#             except:
#                 pass
#
#     def get_url(self):
#         return 'https://techpoint.africa/'
#
#     def confirm_page_crawled(self, url):
#         if self.double_confirm_page_crawled(url, 'http://localhost'):
#             return True
#         elif self.double_confirm_page_crawled(url):
#             return True
#         else:
#             return False
#
#     def double_confirm_page_crawled(self, url, preferred_server=None):
#         print('Calling Endpoint')
#         endpoint = f"{preferred_server if preferred_server else server}/api/third-party-exists"
#         print(url)
#         try:
#             r = requests.post(endpoint, data={'url': url})
#             r_dictionary = json.loads(r.text)
#         except:
#             return True
#
#         if not r_dictionary:
#             print('111111111')
#             return False
#         status = r_dictionary['status']
#         if status == "processed":
#             return True
#         elif status == "raw":
#             return False
#         print('44444444444')
#         return False
#
#     def crawl(self, maximum):
#         links = self.get_page_content()
#         while len(self.urls) < maximum:
#             while len(links):
#                 link = links.pop()
#                 reformed_link = f'{self.get_url()}20{link}'
#                 if 'podcast' in link \
#                         or 'digest' in link \
#                         or link in self.urls \
#                         or self.double_confirm_page_crawled(reformed_link, 'http://localhost'):
#                     continue
#                 if len(self.urls) == maximum:
#                     break
#                 self.urls.append(reformed_link)
#                 self.urls = list(set(self.urls))
#             links = self.click_next_page()
#         print(self.urls)
#         return self.urls
#
#     def get_page_content(self):
#         print('get_page_content waiting for content to load')
#         time.sleep(3)
#         print('Content loaded')
#         body = TechPointBrowser.browser.find_element(By.XPATH, "//body").get_attribute('innerHTML')
#         print('Body copied')
#         hrefs = re.findall('href="/20(.+?)">', str(body))
#         return hrefs
#
#     def click_next_page(self):
#         print('click_next_page Waiting for content to load')
#         time.sleep(10)
#         print('Content loaded clicking button')
#         read_more = '//button[text()="Read More"]'
#         read_more_btn = TechPointBrowser.browser.find_element(By.XPATH, read_more)
#         print('Clicking read_more_btn done')
#         time.sleep(2)
#         read_more_btn.click()
#         time.sleep(6)
#         return self.get_page_content()
