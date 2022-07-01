import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


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
            time.sleep(6)
            Quill.browser.get(f'{Quill.landing_page}')
            Quill.refresh_browser()

        except Exception as e:
            print(e)
            Quill.modal_on = True
            print('An error occured while getting browser')
            # self.close_any_modal()

    @staticmethod
    def refresh_browser():
        Quill.driver.get(f'{Quill.landing_page}')
        time.sleep(8)
        script = "document.getElementById('modes-Expand').children[0].click();"
        Quill.driver.execute_script(script)
        time.sleep(2)

    def click_close_location(self, location, message):
        try:
            close_location = Quill.driver.find_element(By.XPATH, location)
            if close_location:
                print(f'Trying to close {message} modal')
                close_location.click()
                print('modal closed successfully')
                time.sleep(3)
                Quill.modal_on = False
                Quill.death_recovery = 0
        except:
            print(f'Cant find {message} modal')

    def close_any_modal(self, max_attempt=6):
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
                self.click_close_location(premium_green_modal, 'premium_green_modal')
                self.click_close_location(close_go_premium_modes_yellow_modal_btn, 'close_go_premium_modes_yellow_modal_btn')

            except Exception as e:
                print(e)

    def paraphraser(self, to_be_paraphrased):
        to_be_paraphrased = to_be_paraphrased.replace('\n', ' ')
        # print(to_be_paraphrased)
        print('inside paraphraser')
        time.sleep(4)
        print('Getting input text to location')
        inputText = Quill.driver.find_element(By.ID, 'inputText')
        # print('Setting input text to ' + to_be_paraphrased)
        script = "document.getElementById('inputText').innerHTML = `" + to_be_paraphrased + "`;"
        Quill.driver.execute_script(script)
        print('Setting input text to successful')
        time.sleep(2)
        inputText.send_keys(Keys.ENTER)
        print('Pressing enter key')
        time.sleep(5)
        print('Finding quillArticleBtn')
        inputText.send_keys(Keys.ENTER)
        time.sleep(1)
        btn = Quill.driver.find_element(By.XPATH, "//button[contains(@class, 'quillArticleBtn')]")
        print('Clicking quillArticleBtn')
        btn.click()
        continua = True
        dots = '.'
        dots_counter = 0
        while continua:
            dots += "."
            dots_counter += 1
            try:
                time.sleep(3)
                print(f'{dots_counter*3}s Finding quillArticleBtn, loading{dots} \r')
                paraphrase_btn = Quill.driver.find_element(By.XPATH, "//button[contains(@class, 'quillArticleBtn')]")
                if dots_counter*3 >= 240:
                    self.output = []
                    continua = False
                # paraphrase_btn = Quill.driver.find_element(By.XPATH, "//div[contains(@class, 'jss237')]")
                if paraphrase_btn and paraphrase_btn.get_attribute('innerText') == 'Rephrase':
                    print('quillArticleBtn Founding exiting loop \r')
                    time.sleep(6)
                    print('Locating output text for copy')
                    # outputText = Quill.driver.find_element(By.XPATH,
                    #                                              "//div[contains(@style, 'overflow-y:auto;min-height:100%;cursor:text;height:100%;padding-top:20px')]")

                    outputText = Quill.driver.find_element(By.ID, 'editable-content-within-article')
                    # print(f"here is the outputText={outputText.get_attribute('innerText')}")
                    print('Saving output text into outputs')
                    self.counter += 1
                    self.output.append(outputText.get_attribute('innerText'))
                    continua = False

            except:
                pass

    def paraphrase(self, paragraphs):
        self.output = []
        if self.counter >= 2:
            self.counter = 0
            print('About To Refresh Browser')
            Quill.refresh_browser()
            print('Done Refreshing Browser')
        x = 0
        for paragraph in paragraphs:
            try:
                self.paraphraser(paragraph)
                print(f'Paraphrasing {x} value of {len(paragraphs)}')
            except Exception as e:
                print(e)
                time.sleep(3)
                Quill.modal_on = True
                try:
                    print('Trying to close 50 by 50 phrase substitution modal')
                    close_svg = Quill.driver.find_element(By.CSS_SELECTOR, "h2 button")
                    if close_svg:
                        print('close Handle found, closing 50 by 50 phrase substitution modal')
                        close_svg.click()
                        time.sleep(1)
                        Quill.modal_on = False
                        self.paraphraser(paragraph)
                except:
                    print('Cant close modal resulting to close_any_modal')
                    self.close_any_modal()
                    time.sleep(5)
                    try:
                        self.paraphraser(paragraph)
                    except Exception as e:
                        print(e)
                        self.output = []
            x += 1
            while not len(self.output):
                print('Hard refreshing.................................')
                Quill.refresh_browser()
                print('Waiting after Hard refreshing.................................')
                time.sleep(120)
                self.paraphraser(paragraph)
        return paragraphs, self.output
