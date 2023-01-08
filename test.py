import re

from app.consts.const import PARAPHRASING_MISMATCH_ERROR
from app.models.base import Job
from app.tools.blogger import Blogger

# Test the regex
test_string = "https://techcabal.com/2022/12/13/p/"

regex = r"https://techcabal\.com/\d{4}/\d{2}/\d{2}/.+/"
match = re.search(regex, test_string)
if match:
    print("Match found!")
else:
    print("Match not found.")
    
job = Job.get(Job.id == 14)
blogger = Blogger()
blogger.set_state(job.meta)
c_input = blogger.get_rephrase_text()
paraphrased_text = job.meta.get('paraphrased_text', None)
endpoint = job.meta.get('endpoint', None)
print(f'Endpoint is = {endpoint}')
exceptional_tag_map = job.meta.get('exceptional_tag_map', {})
blogger.save_local_content(paraphrased_text, '-output-1-raw')
blogger.save_local_content(paraphrased_text.replace('\n\n\n', '\n'), '-output-1')
try:
    blogger.exceptional_tag_map = exceptional_tag_map
    blogger.remove_stamp_from_tag_map(paraphrased_text)
    blogger.release_exceptional_tags()
    blogger.identify_keyword()
    blogger.post.template = blogger.html_to_text
    blogger.send_post(endpoint, {'job_id': job.id})
    # job.meta['post_data'] = blogger.post_to_string()
    # job.sub_status = ''
    # job.save()
    # print(job.meta['post_data']['template'])
except Exception as e:
    job.sub_status = PARAPHRASING_MISMATCH_ERROR
    # job.meta['paraphrased_text'] = paraphrased_text
    # job.save()
    # print(e)

block = 'Amazon Amazon Amazon Amazon Amazon'
print(block)
block = block.replace('Amazon', 'Aliexpress', 2)
print(block)