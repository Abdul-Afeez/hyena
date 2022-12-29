import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def handle_failure(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
            time.sleep(3)
            Quill.modal_on = True
            Quill.close_any_modal()
            time.sleep(5)
            func(*args, **kwargs)

    return inner


class Quill:
    modal_on = False
    death_recovery = 0
    browser = None
    driver = None
    landing_page = 'https://quillbot.com/'

    def __init__(self):
        self.output = []
        self.counter = 0

    def set_browser(self, browser):
        Quill.browser = browser
        Quill.driver = browser.driver

        # Quill.browser.get(f'{Quill.landing_page}')
        # Quill.refresh_browser()
        # # Quill.browser.get('https://supermart.ng')
        # Quill.browser.get(f'{Quill.landing_page}')
        #
        # return

    def authenticate(self):
        try:
            Quill.driver.get(f'{Quill.landing_page}login?returnUrl=%2F')
            time.sleep(2)
            Quill.driver.get_screenshot_as_file("screenshot.png")

            # email = Quill.driver.find_element(By.XPATH, "//input[@type='text'][1]")
            time.sleep(3)
            script = "document.querySelectorAll('input')[0].value='zeefain54@gmail.com';"
            Quill.driver.execute_script(script)
            # email.send_keys('zeefain54@gmail.com')
            time.sleep(1)

            password = Quill.driver.find_element(By.XPATH, "//input[@type='password'][1]")
            time.sleep(3)
            password.send_keys('11111111')
            time.sleep(3)
            btn = Quill.driver.find_element(By.XPATH,
                                            "//button[contains(@class, 'MuiButtonBase-root auth-btn')]")
            btn.click()
            time.sleep(12)
            Quill.browser.get(f'{Quill.landing_page}')
            Quill.refresh_browser()

        except Exception as e:
            print(e)
            Quill.modal_on = True
            print('An error occured while getting browser')
            # self.close_any_modal()

    @staticmethod
    def refresh_browser():
        print('refresh_browser called')

        Quill.driver.get(f'{Quill.landing_page}')
        time.sleep(8)
        script = "document.getElementById('modes-Expand').children[0].click();"
        Quill.driver.execute_script(script)
        time.sleep(2)

    @staticmethod
    def click_close_location(location, message, xpath=True):
        try:
            if xpath:
                close_location = Quill.driver.find_element(By.XPATH, location)
            else:
                close_location = location
            if close_location:
                print(f'Trying to close {message} modal')
                close_location.click()
                print('modal closed successfully')
                time.sleep(3)
                Quill.modal_on = False
                Quill.death_recovery = 0
        except:
            print(f'Cant find {message} modal')

    @staticmethod
    def close_any_modal(max_attempt=6):
        counter = 0
        while Quill.modal_on:

            try:
                time.sleep(3)
                print('Trying to close_any_modal')
                print(f"counter={counter} of max_attempt={max_attempt}")
                counter += 1
                if Quill.death_recovery >= 6:
                    Quill.browser.close()
                    Quill.modal_on = False

                if counter >= max_attempt:
                    Quill.modal_on = False
                    Quill.death_recovery += 1
                    print(f'Recovering from death channel {Quill.death_recovery}')
                premium_green_modal = "//button[contains(@class, 'MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeLarge css-30h9jf')]"
                close_go_premium_modes_yellow_modal_btn = "//svg[contains(@class, 'MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-10dohqv')]"

                print('About to make the latest close modal engine')

                Quill.click_close_location(premium_green_modal, 'premium_green_modal')
                Quill.click_close_location(close_go_premium_modes_yellow_modal_btn,
                                          'close_go_premium_modes_yellow_modal_btn')
                close_svg = Quill.driver.find_element(By.CSS_SELECTOR, "h2 button")
                Quill.click_close_location(close_svg, 'close_svg', False)
            except Exception as e:
                print(e)

    @handle_failure
    def set_text(self, to_be_paraphrased):
        to_be_paraphrased = to_be_paraphrased.replace('\n', ' ')
        # print(to_be_paraphrased)
        print('inside set_text')
        time.sleep(4)
        print('Getting input text to location')
        inputText = Quill.driver.find_element(By.ID, 'inputText')
        # print('Setting input text to ' + to_be_paraphrased)
        script = "document.getElementById('inputText').innerHTML = `" + to_be_paraphrased + "`;"
        Quill.driver.execute_script(script)
        print('Setting input text to successful')
        inputText.send_keys(Keys.ENTER)
        time.sleep(2)
        inputText.send_keys(Keys.ENTER)
        print('Pressing enter key')
        time.sleep(5)
        inputText.send_keys(Keys.ENTER)
        print('Finding quillArticleBtn')
        inputText.send_keys(Keys.ENTER)

    @staticmethod
    def click_paraphrase_button():
        time.sleep(1)
        btn = Quill.driver.find_element(By.XPATH, "//button[contains(@class, 'quillArticleBtn')]")
        print('Clicking quillArticleBtn')
        btn.click()

    def copy(self):
        self.output = None
        try:
            print('Locating output text for copy')
            output_text = Quill.driver.find_element(By.ID, 'editable-content-within-article')
            print('Saving output text into outputs')
            self.counter += 1
            inner_text = output_text.get_attribute('innerText')
            self.output = inner_text
            return self.output
        except:
            pass

    @staticmethod
    def wait():
        try:
            paraphrase_btn = Quill.driver.find_element(By.XPATH, "//button[contains(@class, 'quillArticleBtn')]")
            if paraphrase_btn and paraphrase_btn.get_attribute('innerText') == 'Rephrase':
                return True
        except:
            pass
        return False



