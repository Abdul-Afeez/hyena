import datetime
import re
import time

import requests
from bs4 import BeautifulSoup
from app.consts.const import SERVER
from app.post.post import Post
from app.tools.keyword_bot import get_fuzzy_similarity, extract_keywords, nlp
from app.tools.validate_url import ValidateUrl


class Blogger(ValidateUrl):
    recognizable_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'p']
    month_dict = {
        'jan': '01',
        'feb': '02',
        'mar': '03',
        'apr': '04',
        'may': '05',
        'jun': '06',
        'jul': '07',
        'aug': '08',
        'sep': '09',
        'oct': '10',
        'nov': '11',
        'dec': '12',
    }

    def __init__(self):
        self.html_to_text = None
        self.posts = []
        self.soup = None

        self.post = None
        self.word_map = []
        self.reverse_word_map_lookup = {}
        self.alt = []
        self.preferred_first_image = False
        self.config = {}

    def find(self, node, find_all=False):
        '''
        :param node:
        :param find_all:
        :return: text or tag or list of tags
        [["h1", "class", "lg:text-4xl", "0"], "text"]]
        '''
        print('node ========= ', node)
        finder = self.soup.find
        node[0][3] = int(node[0][3])
        if find_all:
            finder = self.soup.find_all
        if node[0][1] == 'class':
            output = finder(node[0][0], class_=node[0][2])
        elif node[0][1] == 'id':
            output = finder(node[0][0], id=node[0][2])
        elif node[0][1] == 'property':
            output = finder(node[0][0], property=node[0][2])
        else:
            output = finder(node[0][0])
        if node[1] == 'tag':
            output = output
            # print(output.__dict__)
        elif node[1] == 'text':
            output = output.text
        elif node[1] == 'contents' and node[0][3]:
            output = output.contents[node[0][3]]
        else:
            output = output.attrs[node[1]]
        print(output)
        return output

    def should_not_be_parsed(self):
        bad_signatures = self.config.get('bad_signatures', [])
        print('bad_signatures', bad_signatures)
        output = False
        for bad_signature in bad_signatures:
            try:
                bs = self.find(bad_signature)
                print('bs', bs, str(bs).strip().lower(), '===', bad_signature[2])
                virus = str(bad_signature[2]).strip().lower() in str(bs).strip().lower()
                if virus:
                    output = True
                    break
            except Exception as e:
                print(e)
        return output

    def get_article_date(self):
        raise Exception('Not Implemented')

    def get_main_content(self, soup):
        raise Exception('You must implement this function')

    def get_main_content_terminator(self):
        raise Exception('You must implement this function')

    def terminate(self, terminator=None):
        if not terminator:
            terminator = self.get_main_content_terminator()
        self.html_to_text = self.html_to_text.replace(terminator, f'&&&&{terminator}')
        self.html_to_text = self.html_to_text.split(f'&&&&{terminator}')[0]

    def remove_unwanted_blocks(self, soup):
        raise Exception('You must implement this function')

    def get_h1_class(self):
        return 'single-article-title'

    def get_h1(self):
        raise Exception('Not Implemented')

    def splice(self, start, end):
        try:
            halves = self.html_to_text.split(start)
            self.html_to_text = halves[0] + halves[1].split(end)[1]
        except:
            pass

    def decompose(self, soup, tag, class_):
        try:
            cow_dungs = soup.find_all(tag, class_=class_)
            for cow_dung in cow_dungs:
                cow_dung.decompose()
            return soup
        except:
            pass

    def encapsulate_word_with_tag(self, word, tag, tag_type='hash'):
        if tag_type == 'hash':
            return f'#{tag}#{word}@{tag}@'
        elif tag_type == 'html':
            return f'<{tag}>{word}</{tag}>'
        else:
            pass

    def encapsulate_alt(self, word):
        return f'alt="{word}"'

    def stamp_tag_map(self, word_array, tag):  # e.g ['Why are you Running'], h1
        for raw_word in word_array:
            word = raw_word.replace(f'\\n', ' ')
            word = word.replace(f' ', ' ')
            word = re.sub(r"([a-z]*)\.([@_!\'\"#$%^“&*()<>?/|}’{~:]*)([A-Z]+)", "\g<1>.\g<2> \g<3>",
                          word)  # e.g.L-R to e.g. L-R
            word = re.sub(r"([\'\"^“()<>?/}’{~:]+)([A-Z]+)", "\g<1> \g<2>",
                          word)  # hand. “Connecting to hand. “ Connecting
            word = word.replace(f'\n', ' ').strip()
            self.word_map.append(f'{word}\n')
            lookup_index = len(self.word_map) - 1
            if tag in self.recognizable_tags:
                self.reverse_word_map_lookup[lookup_index] = {'tag': tag, 'lookup': self.
                encapsulate_word_with_tag(raw_word, tag)}
            elif tag.strip() == 'alt':
                self.reverse_word_map_lookup[lookup_index] = {'tag': tag, 'lookup': self.encapsulate_alt(raw_word)}
            elif tag.strip() == 'description':
                self.reverse_word_map_lookup[lookup_index] = {'tag': tag, 'lookup': raw_word}
            else:
                raise Exception('Omooooooooooooooo', raw_word)

    def remove_stamp_from_tag_map(self, body):
        body = body.replace(f'\\n', '\n')
        # body = body.replace(f'\n\n', '\n')
        rephrased = body.split('\n\n\n')
        self.save_local_content(rephrased, '-output-2')

        print(f'self.word_map = {len(self.word_map)} === {len(rephrased)} rephrased')
        self.save_local_content(self.reverse_word_map_lookup, '-reverse_word_map_lookup')

        if len(self.word_map) != len(rephrased):
            raise Exception('Integrity lost during paraphrasing')
        self.save_local_content(rephrased, '-blocks')
        for index, block in enumerate(rephrased):
            block = block.replace('\\n', ' ').strip()
            block = block.replace('\n', ' ').strip()
            # print(index, block)
            reverse_word_map = self.reverse_word_map_lookup[index]
            # print(reverse_word_map)
            tag = reverse_word_map.get('tag')
            if tag in self.recognizable_tags:
                self.html_to_text = self.html_to_text.replace(reverse_word_map.get('lookup'),
                                                              self.encapsulate_word_with_tag(block, tag, 'html'))
            elif tag.strip() == 'alt':
                self.html_to_text = self.html_to_text.replace(reverse_word_map.get('lookup'),
                                                              self.encapsulate_alt(block))
            elif tag.strip() == 'description':
                self.post.description_text = block

        self.html_to_text = self.html_to_text.replace('\n', '')

    def find_all(self, tag):
        return re.findall(f'#{tag}#(.+?)@{tag}@', self.html_to_text)

    def get_rephrase_text(self):
        self.word_map = []
        description_text = (self.post.description_text.replace('"', '').replace(';', ''))
        self.stamp_tag_map(self.find_all('h1'), 'h1')
        self.stamp_tag_map(self.find_all('h2'), 'h2')
        self.stamp_tag_map(self.find_all('h3'), 'h3')
        self.stamp_tag_map(self.find_all('h4'), 'h4')
        self.stamp_tag_map(self.find_all('h5'), 'h5')
        self.stamp_tag_map(self.find_all('h6'), 'h6')
        self.stamp_tag_map(self.find_all('li'), 'li')
        self.stamp_tag_map(self.find_all('p'), 'p')
        self.stamp_tag_map(self.alt, 'alt')
        self.stamp_tag_map([description_text], 'description')
        c_input = '\\n\\n\\n'.join(self.word_map)
        self.save_local_content(self.html_to_text, '-paraphrased')
        self.save_local_content(c_input, '-input')
        self.save_local_content(self.word_map, '-word_map')
        return c_input

    def get_description(self, soup):
        print('Default Blogger get_description')
        return soup.find('meta', property="og:description").attrs['content']

    def secure_image(self, main_content):
        images = main_content.find_all('img')
        main_content = str(main_content)
        counter = 0
        self.alt = []
        for image in images:
            try:
                if counter > 10:
                    break
                attrs = image.attrs
                attr_keys = attrs.keys()
                alt_text = attrs["alt"] if "alt" in attr_keys else None
                image_title = attrs["title"] if "title" in attr_keys else None
                alt_text = alt_text or image_title
                if alt_text:
                    self.alt.append(alt_text.replace('"', '').replace(';', ''))
                alt_ppt = f" alt=\"{alt_text}\"" if alt_text else None
                main_content = main_content.replace(str(image),
                                                    f"<img src=\"{attrs['src']}\"{alt_ppt if alt_ppt else ''} />")
                counter += 1
            except:
                image.decompose()
        main_content = re.sub(r"(.*)<img(.*)src(.*)/>(.*)", "\g<1><p>#img#\g<2>src\g<3>@img@</p>\g<4>",
                              str(main_content))
        main_content = re.sub(r"(.*)>\n</img>(.*)", "\g<1>/>\g<2>", main_content)
        main_content = re.sub(r"(.*)<img(.*)/>(.*)", "\g<1><p>#img#\g<2>@img@</p>\g<3>", main_content)
        main_content = main_content.replace('<li><a', '<a')  # to fix issue with li a img
        main_content = main_content.replace('</a></li>', '</a>')
        main_content = main_content.replace('<li class="blocks-gallery-item"><figure>',
                                            '<figure>')  # to fix issue with li a img
        main_content = main_content.replace('</figure>', '</figure>')
        return main_content

    def set_description_image(self, main_content):
        all_images = main_content.find_all('img')
        if all_images:
            for image in all_images:
                try:
                    self.post.description_image = image.attrs["src"]
                    break
                except:
                    self.post.description_image = 'https://cdn.pixabay.com/photo/2018/05/02/20/49/technology-3369659_960_720.jpg'
        else:
            self.post.description_image = 'https://cdn.pixabay.com/photo/2018/05/02/20/49/technology-3369659_960_720.jpg'
        print(self.post.description_image)

    def extract(self, url, html):
        '''
        To extract the various HTML tags from the content parsed
        :param url:
        :param html:
        :return: data = {
                'url': self.post.url,
                'title': self.post.title,
                'keywords': self.post.keywords,  # needs rework
                'description_image': self.post.description_image,
                'description_text': self.post.description_text,  # needs rework
                'template': f'{self.html_to_text}',  # needs rework
                'created_at': self.post.created_at,
                'document': document
            }
        '''
        print('crawling 123')
        # print(self.browser.history)
        self.soup = BeautifulSoup(html, "html.parser")
        if self.should_not_be_parsed():
            print(f"Can't parse {url}, Ignored!!!")
            return False
        self.post = Post()
        self.post.url = url
        self.post.description_text = self.get_description(self.soup)
        try:
            self.post.created_at = self.get_article_date()
        except:
            self.post.created_at = datetime.datetime.now()
            print('error processing date')
        self.post.title = self.get_h1()
        print('Getting main content')
        try:
            main_content = self.get_main_content(self.soup)
        except Exception as e:

            print('Error occured', e)
            return False
        print('Setting description image')
        self.set_description_image(main_content)
        print('remove_unwanted_blocks')
        main_content = self.remove_unwanted_blocks(main_content)
        # print(main_content)
        return main_content
        main_content = self.secure_image(main_content)
        main_content = main_content.replace('<br>', ' ')
        main_content = main_content.replace('<br/>', ' ')
        self.save_local_content(main_content, 'main-content')
        main_content = BeautifulSoup(main_content, "html.parser")
        print('Escaping tags')
        document = {}
        for each_tag in self.recognizable_tags:  # ['h1', 'h2', 'p' ......]
            for tag in main_content.find_all(each_tag):  # ['h1': [<h1>Block buster</h1>]]
                try:
                    if not tag.text:  # <h1></h1>
                        tag.decompose()
                    else:
                        tag.string = f"#{each_tag}#{tag.text}@{each_tag}@"
                except:
                    tag.string = f"#{each_tag}#{tag.text}@{each_tag}@"  # <h1>#h1#Blockbuster@h1@</h1>
                document[each_tag] = f"{document.get(each_tag, '')} {tag.text}".replace(f"#{each_tag}#", '') \
                    .replace(f"@{each_tag}@", '')  # Blockbuster
                document[each_tag] = re.sub(r"(.*)#img#.*src=(.*)@img@(.*)", f"\g<1> \g<3>",
                                            document[each_tag])
        self.html_to_text = str(main_content.text)
        print(f'Still going through {url}')
        self.html_to_text = re.sub(r"(.*)#p##img#.*src=(.*)@img@@p@(.*)", f"\g<1><img src=\g<2> />\g<3><div class='text-small d-inline image-source'><i>{self.config.get('image_source', '')}</i></div>",
                                   self.html_to_text)
        print('Paraphrasing')
        try:
            self.clean_empty_tags()
            self.terminate()
            data = {
                'url': self.post.url,
                'title': self.post.title,
                'keywords': self.post.keywords,  # needs rework
                'description_image': self.post.description_image,
                'description_text': self.post.description_text,  # needs rework
                'template': f'''{self.html_to_text}''',  # needs rework
                'created_at': self.post.created_at,
                'document': document
            }
            # print(data)
            return data
            # Update parse to ran
            # Save new job with pending paraphrase

        except Exception as e:
            # self.save_local_content(str(e), '-error')
            # Update parse to FAILED
            # self.send_post(status='failed')
            print(e)

    def set_state(self, data):
        self.post = Post()
        self.post.url = data.get('url', '')
        self.post.title = data.get('title', '')
        self.post.keywords = data.get('keywords', '')
        self.post.description_text = data.get('description_text', '')
        self.post.description_image = data.get('description_image', '')
        self.post.template = data.get('template', '')
        self.post.created_at = data.get('created_at', '')
        self.html_to_text = self.post.template

    def rephrase(self):
        # return
        self.identify_keyword()
        self.save_local_content(self.html_to_text, '-template')
        self.post.template = self.html_to_text
        self.send_post()

    def identify_keyword(self):
        last_soup = BeautifulSoup(self.html_to_text, "html.parser")
        h1 = last_soup.find('h1')
        if h1:
            h1.decompose()
        passage = last_soup.text
        passage = re.sub(r"#(.*)#", "", passage)
        passage = re.sub(r"@(.*)@", "", passage)
        splitted_title = self.post.title.split(' ')
        counter = 0
        keywords = []
        raw_keywords = []
        token = ''
        for spl in splitted_title:
            if counter == 2:
                token += f' {spl}'
                # print(f'token {token}')
                raw_keywords += get_fuzzy_similarity(token, extract_keywords(nlp, passage))
                token = ''
                counter = 0
            else:
                token += f' {spl}'
                counter += 1
        for raw_keyword in raw_keywords:
            keywords.append(raw_keyword[0])
        keywords.sort()
        keywords = list(set(keywords))
        for index, keyword in enumerate(keywords):
            self.post.keywords += f', {keyword}' if index > 0 else f'{keyword}'
            keyword_length = len(keyword.split(' '))
            if keyword_length <= 2:
                self.html_to_text = self.html_to_text.replace(f" {keyword} ", f" <strong>{keyword}</strong> ")
            else:
                self.html_to_text = self.html_to_text.replace(f" {keyword} ", f" <strong>{keyword}</strong> ")
            if index > 20:
                break

    def save_local_content(self, content, index=None):
        folder_name = f'build/{self.get_post_folder_name(self.post.title)}'
        self.save_content(content, index, folder_name)

    def post_to_string(self):
        return {
            'url': self.post.url,
            'title': self.post.title,
            'keywords': self.post.keywords,
            'description_image': self.post.description_image,
            'description_text': self.post.description_text,
            'template': self.post.template,
            'created_at': self.post.created_at
        }

    def send_post(self, endpoint, status=None):
        data = self.post_to_string()
        if status:
            data['status'] = status
            print(f"Sending data")
            # r = requests.post(f"{SERVER}/api/save-{status}", data)
            endpoint = endpoint.split('article')[0]
            r = requests.post(f"{endpoint}-{status}", data)
        else:
            r = requests.post(f"{endpoint}", data)

            print(f"Sending data")

        print(f"Result is {r.text}")

    def replacer(self, tag, tags_in, tags_out):
        time.sleep(2)
        x = 0
        for tag_in in tags_in:
            self.html_to_text = self.html_to_text.replace(f"#{tag}#{tag_in}@{tag}@", f"<{tag}>{tags_out[x]}</{tag}>")
            x += 1

    def clean_empty_tags(self):
        self.html_to_text = self.html_to_text.replace("\n", '')
        for tag in self.recognizable_tags:
            self.html_to_text = self.html_to_text.replace(f"#{tag}#@{tag}@", '')
            self.html_to_text = self.html_to_text.replace(f"#{tag}#", f'\n#{tag}#')
            self.html_to_text = self.html_to_text.replace(f"@{tag}@", f'@{tag}@\n')
