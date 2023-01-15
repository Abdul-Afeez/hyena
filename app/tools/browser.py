import re
import time
from selenium import webdriver

from selenium.webdriver import DesiredCapabilities
from fake_useragent import UserAgent

from app.threads.mediator import Printer


class Browser:
    driver = None
    session_id = None
    desired_capabilities = DesiredCapabilities.CHROME
    history = []
    # options.add_argument("start-maximized")
    # options.add_argument("disable-infobars")
    # options.add_argument("--disable-extensions")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-application-cache')
    # options.add_argument('--disable-gpu')
    # options.add_argument("--disable-dev-shm-usage")
    def __init__(self):
        self.printer = Printer
    @staticmethod
    def set_desired_capabilities(desired_capabilities):
        Browser.desired_capabilities = desired_capabilities

    @staticmethod
    def get_driver():
        Browser.set_desired_capabilities(Browser.desired_capabilities)
        try:
            if not Browser.session_id:
                try:
                    ua = UserAgent()
                    user_agent = ua.random

                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_experimental_option("prefs",
                                                           {"profile.managed_default_content_settings.images": 2})
                    # chrome_options.add_argument("--window-size=1366,768")
                    # chrome_options.add_argument("--window-size=1366,400")
                    chrome_options.add_argument("--disable-infobars")
                    chrome_options.add_argument("--disable-notifications")
                    # chrome_options.add_argument("--disable-extensions")
                    # chrome_options.add_argument("--proxy-server='direct://'")
                    # chrome_options.add_argument("--proxy-bypass-list=*")
                    chrome_options.add_argument("--start-maximized")
                    # chrome_options.add_argument('--headless')
                    chrome_options.add_argument('--disable-gpu')
                    chrome_options.add_argument('--disable-dev-shm-usage')
                    chrome_options.add_argument('--no-sandbox')
                    # chrome_options.add_argument('--ignore-certificate-errors')
                    # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
                    # chrome_options.add_argument(f'user-agent={user_agent}')
                    print(user_agent)
                    chrome_options.add_argument(f'user-agent={user_agent}')

                    print('Connecting to web driver.......')
                    Browser.driver = webdriver.Remote("http://selenium-hub:4444", desired_capabilities=Browser.desired_capabilities, options=chrome_options)
                    # Browser.driver = webdriver.Chrome(executable_path="app/tools/drivers/chromedriver", chrome_options=chrome_options)
                    if not Browser.session_id:
                        Printer.basic_print(f'saving session_id: ====== {Browser.driver.session_id}')
                        Browser.session_id = Browser.driver.session_id
                except Exception as e:
                    print(e)
            else:
                Browser.driver.session_id = Browser.session_id
        except Exception as e:
            print(e)

    @staticmethod
    def get(target_link):
        Printer.basic_print(f'Visiting {target_link}')
        if target_link not in Browser.history:
            Browser.history.append(target_link)
        Browser.driver.get(target_link)
        Printer.basic_print(f'Visited {target_link}')

    @staticmethod
    def open_link_in_new_tab(target_link):
        try:
            Printer.basic_print(f'Opening {target_link} in new tab')
            driver = Browser.driver
            driver.execute_script("window.open('');")
            # Browser.switch_to_tab(link)
            time.sleep(2)
            Printer.basic_print(f'len(Browser.history) == {len(Browser.history)}')
            driver.switch_to.window(driver.window_handles[len(Browser.history)])
            Browser.get(target_link)
            Printer.basic_print(f'Opened {target_link} in new tab')
            Printer.basic_print(f'len(Browser.history) == {len(Browser.history)}')
        except Exception as e:
            print('The problem has been handled, but we are closing the orphan tab ................................')
            print(e)
        # Switch to the new window

    @staticmethod
    def switch_to_tab(target_link):
        Printer.basic_print(f'Switching tab to {target_link}')
        driver = Browser.driver
        driver.switch_to.window(driver.window_handles[Browser.history.index(target_link)])
        Printer.basic_print(f'Switched tab to {target_link}')
        time.sleep(2)

    @staticmethod
    def close_tab(target_link):
        driver = Browser.driver
        Browser.switch_to_tab(target_link)
        Printer.basic_print(f'Closing tab {target_link}')
        del Browser.history[Browser.history.index(target_link)]
        time.sleep(3)
        try:
            driver.close()
        except Exception as e:
            print(e)
        Printer.basic_print(f'Closed tab {target_link}')
        time.sleep(1)

#
# links = ['https://supermart.ng', 'https://google.com', 'https://techcabal.com', 'https://techcrunch.com']
#
# print('Trying out tab switching')
# print('Creating firefox instance')
# firefox = Browser()
# print('Getting firefox')
# Browser.get_driver()
# print('Got driver handle')
# time.sleep(4)
# firefox.get(links[0])
#
# firefox.open_link_in_new_tab(links[1])
# time.sleep(2)
#
# firefox.open_link_in_new_tab(links[2])
# time.sleep(2)
#
# firefox.open_link_in_new_tab(links[3])
# time.sleep(2)
#
# for link in links:
#     firefox.switch_to_tab(link)
#     time.sleep(2)
#
#
# for link in links:
#     firefox.switch_to_tab(link)
#     firefox.close_tab(link)
