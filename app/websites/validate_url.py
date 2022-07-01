import json
import os
import re
import time

import requests

from app.consts.const import SERVER, LOCALHOST


class ValidateUrl:

    def get_post_folder_name(self, title):
        folder_name = re.sub(r"(.*)([@_!\'\"#$%^“&*()<>?/|}’{~:]*)(.*)", "\g<1>-\g<3>", title)
        folder_name = folder_name.replace('/', '')
        return folder_name

    def save_content(self, content, index=None, folder_name='any'):
        try:
            if not os.path.isdir(folder_name):
                os.mkdir(folder_name)
        except Exception as e:
            print(e)
        if index:
            file1 = open(f'{folder_name}/main_content{index}.txt', 'w')
        else:
            file1 = open(f'{folder_name}/main_content{index}.txt', 'w')
        file1.writelines(str(content))
        file1.close()
        # print('Saving Post')

    def confirm_page_crawled(self, url):
        if self.double_confirm_page_crawled(url, LOCALHOST):
            return True
        elif self.double_confirm_page_crawled(url):
            return True
        else:
            return False

    def double_confirm_page_crawled(self, url, preferred_server=None):
        print('Calling Endpoint')
        endpoint = f"{preferred_server if preferred_server else SERVER}/api/third-party-exists"
        print(url)
        time.sleep(1)
        try:
            r = requests.post(endpoint, data={'url': url})
            r_dictionary = json.loads(r.text)
        except:
            return True

        if not r_dictionary:
            print('111111111')
            return False
        status = r_dictionary['status']
        if status == "processed":
            return True
        elif status == "raw":
            print('3333333333333')
            return False
        print('44444444444')
        return False