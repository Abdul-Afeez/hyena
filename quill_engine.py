import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Quill:
    browser = None
    modal_on = False
    def __init__(self):
        self.output = []

    def close_any_modal(self, max_attempt=4):
        counter = 0
        while Quill.modal_on:
            print(f"counter={counter} of max_attempt={max_attempt}")
            counter += 1
            if counter >= max_attempt:
                Quill.browser.refresh()
            try:
                time.sleep(3)
                print('Trying to close_any_modal')
                close_modal_btn = Quill.browser.find_element(By.XPATH,
                                                                "//button[contains(@style, 'position: absolute; top: 0px; right: 0px; padding: 8px;')]")
                if close_modal_btn:
                    print('close_any_modal handle found closing modal')
                    close_modal_btn.click()
                    print('modal closed successfully')
                    time.sleep(3)
                    Quill.modal_on = False
            except:
                pass

    def paraphraser(self, to_be_paraphrased):
        print('inside paraphraser')
        time.sleep(3)
        print('Getting input text to location')
        inputText = Quill.browser.find_element(By.ID, 'inputText')
        print('Setting input text to ' + to_be_paraphrased)
        script = "document.getElementById('inputText').innerHTML = \"" + to_be_paraphrased + "\";"
        Quill.browser.execute_script(script)
        print('Setting input text to successful')
        inputText.send_keys(Keys.ENTER)
        print('Pressing enter key')
        time.sleep(7)
        # btn = browser.find_element(By.CSS_SELECTOR, "div div div  div div div div button")
        print('Finding quillArticleBtn')
        btn = Quill.browser.find_element(By.XPATH, "//button[contains(@class, 'quillArticleBtn')]")
        print('Clicking quillArticleBtn')
        btn.click()
        continua = True
        while continua:
            try:
                print('Finding quillArticleBtn, loading...')
                paraphrase_btn = Quill.browser.find_element(By.XPATH, "//button[contains(@class, 'quillArticleBtn')]")

                # paraphrase_btn = Quill.browser.find_element(By.XPATH, "//div[contains(@class, 'jss237')]")
                if paraphrase_btn and paraphrase_btn.get_attribute('innerText') == 'Rephrase':
                    print('quillArticleBtn Founding exiting loop')
                    time.sleep(2)
                    print('Locating output text for copy')
                    # outputText = Quill.browser.find_element(By.XPATH,
                    #                                              "//div[contains(@style, 'overflow-y:auto;min-height:100%;cursor:text;height:100%;padding-top:20px')]")

                    outputText = Quill.browser.find_element(By.ID, 'editable-content-within-article')
                    print(f"here is the outputText={outputText.get_attribute('innerText')}")
                    print('Saving output text into outputs')
                    self.output.append(outputText.get_attribute('innerText'))
                    continua = False

            except:
                pass



    def set_browser(self):
        if not Quill.browser:
            try:
                chrome_options = webdriver.ChromeOptions()
                # chrome_options.add_argument("--window-size=1920,1080")
                # chrome_options.add_argument("--disable-extensions")
                # chrome_options.add_argument("--proxy-server='direct://'")
                # chrome_options.add_argument("--proxy-bypass-list=*")
                # chrome_options.add_argument("--start-maximized")
                # chrome_options.add_argument('--headless')
                # chrome_options.add_argument('--disable-gpu')
                # chrome_options.add_argument('--disable-dev-shm-usage')
                # chrome_options.add_argument('--no-sandbox')
                # chrome_options.add_argument('--ignore-certificate-errors')
                # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
                # chrome_options.add_argument(f'user-agent={user_agent}')
                chrome_options.headless = False
                Quill.browser = webdriver.Chrome(executable_path="./drivers/chromedriver", options=chrome_options)
                Quill.browser.get('https://quillbot.com/login?returnUrl=%2F')
                time.sleep(2)
                Quill.browser.get_screenshot_as_file("screenshot.png")

                # email = Quill.browser.find_element(By.XPATH, "//input[@type='text'][1]")
                time.sleep(3)
                script = "document.querySelectorAll('input')[0].value='zeefain54@gmail.com';"
                Quill.browser.execute_script(script)
                # email.send_keys('zeefain54@gmail.com')
                time.sleep(1)

                password = Quill.browser.find_element(By.XPATH, "//input[@type='password'][1]")
                time.sleep(3)
                password.send_keys('11111111')

                time.sleep(1)
                btn = Quill.browser.find_element(By.XPATH,
                                                 "//button[contains(@class, 'MuiButtonBase-root MuiButton-root MuiButton-contained auth-btn MuiButton-containedPrimary MuiButton-fullWidth')]")
                btn.click()
                time.sleep(4)

                Quill.browser.get('https://quillbot.com/')
                time.sleep(1)
            except:
                Quill.modal_on = True
                print('An error occured while getting browser')
                self.close_any_modal()

    def paraphrase(self, paragraphs):
        self.output = []
        x = 0
        for paragraph in paragraphs:
            try:
                self.paraphraser(paragraph)
                print(f'Paraphrasing {x} value of {len(paragraphs)}')
            except:
                time.sleep(3)
                Quill.modal_on = True
                try:
                    print('Trying to close 50 by 50 phrase substitution modal')
                    close_svg = Quill.browser.find_element(By.CSS_SELECTOR, "h2 button")
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
                    self.paraphraser(paragraph)
            x += 1
        return paragraphs, self.output
