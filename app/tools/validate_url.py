import json
import os
import re
import time

import requests

from app.consts.const import SERVER, LOCALHOST
from app.models.base import Job


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
        try:
            if index:
                file1 = open(f'{folder_name}/main_content{index}.txt', 'w')
            else:
                file1 = open(f'{folder_name}/main_content{index}.txt', 'w')
            file1.writelines(str(content))
            file1.close()
        except Exception as e:
            print(e)
        # print('Saving Post')

    def confirm_page_crawled(self, url):
        job_exist = Job.select().where((Job.reference_url == url) | (Job.url == url))
        if job_exist:
            return True
        return False
