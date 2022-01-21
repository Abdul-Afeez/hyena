import json
import math
import re
import time

import requests
from bs4 import BeautifulSoup

from keyword_bot import extract_keywords, nlp, get_fuzzy_similarity
from quill_engine import Quill

server = "http://104.248.169.198"
# server = "http://localhost"
quill = Quill()


class Post:
    def __init__(self):
        self.url = ''
        self.title = ''
        self.keywords = ''
        self.description_image = ''
        self.description_text = ''
        self.template = ''

    def __str__(self):
        return self.title

    def __add__(self, other):
        if type(other) == type(dict()):
            for prop, value in other.items():
                self.__dict__[prop] = value
        else:
            for prop, value in other.__dict__.items():
                self.__dict__[prop] = value
        return self


class Blogger:

    def __init__(self):
        self.name = 'Blogger'
        self.html_to_text = None
        self.url = self.get_url()
        self.unvisited_latest = []
        self.posts = []
        self.old_failed_posts = {}
        self.post = None
        self.description_images = {}
        self.alt = []
        self.preferred_first_image = False

    def get_url(self):
        raise Exception('Y')

    def set_latest_post(self):
        raise Exception('Y')

    def confirm_page_crawled(self, url):
        print('Calling Endpoint')
        endpoint = f"{server}/api/third-party-exists"
        print(url)
        try:
            r = requests.post(endpoint, data={'url': url})
            # print(r.text)
            # r_dictionary = r.json()
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
            self.old_failed_posts[url] = r_dictionary
            return False
        print('44444444444')
        return False

    def crawl_and_publish(self):
        for unvisited_latest in self.unvisited_latest:
            self.crawl(unvisited_latest)
            # break

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

    def rephrase_text(self):
        h1 = re.findall('#h1#(.+?)@h1@', self.html_to_text)
        h2 = re.findall('#h2#(.+?)@h2@', self.html_to_text)
        h3 = re.findall('#h3#(.+?)@h3@', self.html_to_text)
        h4 = re.findall('#h4#(.+?)@h4@', self.html_to_text)
        h5 = re.findall('#h5#(.+?)@h5@', self.html_to_text)
        h6 = re.findall('#h6#(.+?)@h6@', self.html_to_text)
        p = re.findall('#p#(.+?)@p@', self.html_to_text)
        li = re.findall('#li#(.+?)@li@', self.html_to_text)
        description_text = (self.post.description_text.replace('"', '').replace(';', ''))

        description = [description_text]
        alt = self.alt

        walked = 0
        work = h1+h2+h3+h4+h5+h6+p+li+description+alt
        work_distance = len(work)
        # self.save_local_content(f'li = {li} \n\n\n description={self.post.description_text} \n\n'
        #                         f'alt_in, {self.alt}')
        # raise Exception('BYE')

        quill.set_browser(work_distance)

        print('description_in')
        description_in, description_out = quill.paraphrase(description)
        if description_out:
            print('00000000000000AAAAAAAAAAAAA')
            self.post.description_text = description_out[0]
            print('1111111111111111BBBBBBBBBBB')

        print('alt_in', self.alt)
        alt_in, alt_out = quill.paraphrase(alt)
        try:
            for index, alt in enumerate(alt_in):
                self.html_to_text = self.html_to_text.replace(f"alt=\"{alt}\"", f"alt=\"{alt_out[index]}\"")
        except:
            raise Exception('ppppppppppppppppp')

        h1_in, h1_out = quill.paraphrase(h1)
        print('h1_in')
        self.replace('h1', h1_in, h1_out)
        if h1_out:
            print('00000000000000CCCCCCCCCCCCCCC')
            self.post.title = h1_out[0]

        h2_in, h2_out = quill.paraphrase(h2)
        self.replace('h2', h2_in, h2_out)
        print('h2_in')

        h3_in, h3_out = quill.paraphrase(h3)
        self.replace('h3', h3_in, h3_out)

        h4_in, h4_out = quill.paraphrase(h4)
        self.replace('h4', h4_in, h4_out)

        h5_in, h5_out = quill.paraphrase(h5)
        self.replace('h5', h5_in, h5_out)

        h6_in, h6_out = quill.paraphrase(h6)
        self.replace('h6', h6_in, h6_out)

        print('p_in')
        p_in, p_out = quill.paraphrase(p)
        self.replace('p', p_in, p_out)

        print('li_in')
        li_in, li_out = quill.paraphrase(li)
        self.replace('li', li_in, li_out)

        print('DOne replacessssssssssssssssss')

    def get_description(self, soup):
        return soup.find('meta', property="og:description").attrs['content']

    def secure_image(self, main_content):
        images = main_content.find_all('img')
        main_content = str(main_content)
        counter = 0
        self.alt = []
        for image in images:
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
        main_content = re.sub(r"(.*)<img(.*)/>(.*)", "\g<1><p>#img#\g<2>@img@</p>\g<3>", str(main_content))
        return main_content

    def crawl(self, unvisited_latest):
        old_failed_post_keys = self.old_failed_posts.keys()
        already_paraphrased = None
        if unvisited_latest in old_failed_post_keys:
            already_paraphrased = self.old_failed_posts[unvisited_latest]
        if not already_paraphrased:
            page = requests.get(unvisited_latest)
            soup = BeautifulSoup(page.content, "html.parser")
            self.post = Post()
            self.post.url = unvisited_latest
            self.post.description_text = self.get_description(soup)
            self.post.title = soup.find('h1', class_=self.get_h1_class()).text
            main_content = self.get_main_content(soup)
            first_image = main_content.find('img')
            if self.preferred_first_image or (not self.post.description_image and first_image):
                self.post.description_image = first_image.attrs["src"]
            else:
                self.post.description_image = self.description_images[unvisited_latest]

            main_content = self.remove_unwanted_blocks(main_content)

            main_content = self.secure_image(main_content)
            main_content = BeautifulSoup(main_content, "html.parser")
            data = {
                'text': '',
                'h1': []
            }
            for each_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'p']:
                for tag in main_content.find_all(each_tag):
                    try:
                        if not tag.text:
                            tag.decompose()
                        else:
                            tag.string = f"#{each_tag}#{tag.text.splitlines()[0]}@{each_tag}@"
                    except:
                        tag.string = f"#{each_tag}#{tag.text}@{each_tag}@"

            self.html_to_text = str(main_content.text)
            print(f'Still going through {unvisited_latest}')
            self.html_to_text = re.sub(r"(.*)#p##img#.*src=(.*)@img@@p@(.*)", f"\g<1><img src=\g<2> /><br /><span>Source: {self.name}</span>\g<3>",
                                       self.html_to_text)
            # self.save_local_content(self.html_to_text)
            # raise Exception('Done')
            try:
                self.clean_empty_tags()
                self.terminate()
                self.rephrase_text()
                self.identify_keyword()
                self.save_local_content(self.html_to_text)
            except Exception as e:
                print(e)
            self.post.template = self.html_to_text
        else:
            self.post = Post()
            self.post = self.post + already_paraphrased
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
                print(f'token {token}')
                raw_keywords += get_fuzzy_similarity(token, extract_keywords(nlp, passage))
                token = ''
                counter = 0
            else:
                token += f' {spl}'
                counter += 1
        for raw_keyword in raw_keywords:
            keywords.append(raw_keyword[0])
        keywords.sort()
        for keyword in keywords:
            self.post.keywords += f', {keyword}'
            keyword_length = len(keyword.split(' '))
            if keyword_length <= 2:
                self.html_to_text = self.html_to_text.replace(f" {keyword} ", f" <strong>{keyword}</strong> ")
            else:
                self.html_to_text = self.html_to_text.replace(f" {keyword} ", f" <strong>{keyword}</strong> ")

    def save_local_content(self, content):
        file1 = open('main_content.txt', 'w')
        file1.writelines(str(content))
        file1.close()

        print('Saving Post')

    def send_post(self):
        data = {
            'url': self.post.url,
            'title': self.post.title,
            'keywords': self.post.keywords,
            'image': self.post.description_image,
            'description': self.post.description_text,
            'template': self.post.template,
        }
        print(f"Sending {data}")

        r = requests.post(f"{server}/api/save-article", data)
        print(f"Result is {r.text}")

    def replace(self, tag, tags_in, tags_out):
        time.sleep(2)
        x = 0
        for tag_in in tags_in:
            self.html_to_text = self.html_to_text.replace(f"#{tag}#{tag_in}@{tag}@", f"<{tag}>{tags_out[x]}</{tag}>")
            x += 1

    def clean_empty_tags(self):
        self.html_to_text = self.html_to_text.replace("\n", '')
        for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'p']:
            self.html_to_text = self.html_to_text.replace(f"#{tag}#@{tag}@", '')
            self.html_to_text = self.html_to_text.replace(f"#{tag}#", f'\n#{tag}#')
            self.html_to_text = self.html_to_text.replace(f"@{tag}@", f'@{tag}@\n')


class TechPoint(Blogger):

    def __init__(self):
        super().__init__()
        self.name = 'Techpoint'

    def get_url(self):
        return 'https://techpoint.africa/'

    def get_h1_class(self):
        return 'entry-title'

    def get_main_content(self, soup):
        main = soup.find('div', id='main-content')
        return main.contents[1]

    def remove_unwanted_blocks(self, soup):
        soup = self.decompose(soup, 'div', 'ss-inline-share-wrapper')
        soup = self.decompose(soup, 'div', 'abfd-container')
        soup = self.decompose(soup, 'p', 'et_pb_title_meta_container')
        soup = self.decompose(soup, 'p', 'abfd_et_pb_row')
        soup = self.decompose(soup, 'p', 'abfd-photograph')
        soup = self.decompose(soup, 'p', 'abfd-biography')
        soup = self.decompose(soup, 'p', 'ss-social-icons-container')
        return soup

    def get_main_content_terminator(self):
        return '#h3#Recent News'

    def terminate(self, terminator=None):
        super().terminate()
        super().terminate("Subscribe Connect")

    def set_latest_post(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        raw_links = soup.find_all('h4', class_="entry-title")
        x = 0
        for raw_link in raw_links:
            url = raw_link.find('a').attrs['href']
            # url = "https://disrupt-africa.com/2021/12/31/applications-open-for-8th-tony-elumelu-entrepreneurship-programme/"
            crawled = self.confirm_page_crawled(url)
            if not crawled:
                self.unvisited_latest.append(url)
                image = raw_link.parent.find('img', class_='webpexpress-processed')
                image_attrs = image.attrs.keys()
                if 'src' in image_attrs:
                    self.description_images[url] = image.attrs['src']
                x += 1
        # self.save_local_content()
                # break


class TechCabal(Blogger):
    def __init__(self):
        super().__init__()
        self.name = 'TechCabal'
        self.preferred_first_image = True
    def get_h1_class(self):
        return 'single-article-title'

    def remove_unwanted_blocks(self, soup):
        soup = self.decompose(soup, 'div', 'single-article-info')
        soup = self.decompose(soup, 'div', 'single-article-category')
        soup = self.decompose(soup, 'div', 'list-newsletter-form shortcode')
        return soup

    def get_url(self):
        return 'https://techcabal.com/'

    def get_main_content(self, soup):
        main = soup.find('main')
        return main.contents[2]

    def get_main_content_terminator(self):
        return 'Share this article'

    def set_latest_post(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        raw_articles = soup.find_all('article', class_="article-list-item")
        x = 0
        for raw_article in raw_articles:
            print('Trying to curl page')
            url = raw_article.find('a', class_="article-list-title").attrs['href']
            category_link = raw_article.find('a', class_="article-list-category").attrs['href']
            print(f'category_link {category_link}')
            if 'newsletter' in category_link:
                continue
            else:
                pass
            print(url)
            crawled = self.confirm_page_crawled(url)
            if not crawled:
                self.unvisited_latest.append(url)
                self.description_images[url] = soup.find('img', class_='wp-post-image').attrs["src"]
                x += 1
                # break
            print('Sleeping for 2 seconds')
        self.save_local_content(self.unvisited_latest)
        # raise Exception('Done')
            # time.sleep(2)

    def clean_empty_tags(self):
        super().clean_empty_tags()


class DisruptAfrica(Blogger):
    def __init__(self):
        super().__init__()
        self.name = 'DisruptAfrica'
        self.preferred_first_image = True

    def get_h1_class(self):
        return 'post-title'

    def remove_unwanted_blocks(self, soup):
        soup = self.decompose(soup, 'div', 'post-meta cf')
        soup = self.decompose(soup, 'a', 'comments')
        return soup

    def get_url(self):
        return 'https://disrupt-africa.com/'

    def get_main_content(self, soup):
        main = soup.find('div', class_='main-content')
        return main.contents[1]

    def get_main_content_terminator(self):
        return 'Share.'

    def secure_image(self, main_content):
        main_content = super().secure_image(main_content)
        main_content = re.sub(r"(.*)>\n</img>(.*)", "\g<1>/>\g<2>", main_content)
        main_content = re.sub(r"(.*)<img(.*)/>(.*)", "\g<1><p>#img#\g<2>@img@</p>\g<3>", main_content)
        return main_content

    def set_latest_post(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")

        raw_articles = soup.find('ul', class_="posts-list").find_all('li')
        for raw_article in raw_articles:
            a = raw_article.find('a')
            url = a.attrs['href']
            crawled = self.confirm_page_crawled(url)
            if not crawled:
                self.unvisited_latest.append(url)

        raw_articles = soup.find_all('a', class_='title')
        for raw_article in raw_articles:
            url = raw_article.attrs['href']
            crawled = self.confirm_page_crawled(url)
            if not crawled:
                self.unvisited_latest.append(url)

        cow_dungs = soup.find_all('span', class_='cat cat-title cat-38')
        for cow_dung in cow_dungs:
            cow_dung.decompose()

        raw_articles = soup.find_all('article')
        for raw_article in raw_articles:
            a = raw_article.find('a')
            url = a.attrs['href']
            if 'category' in url:
                continue
            crawled = self.confirm_page_crawled(url)
            if not crawled:
                self.unvisited_latest.append(url)

    def clean_empty_tags(self):
        super().clean_empty_tags()


virus = """





#p#Social Media@p@


#h1##Twitterban update: A precedent for future shutdowns?@h1@

#p##img# src="https://techpoint.africa/wp-content/uploads/2021/06/Featured-Image-1.1-01.jpeg" alt="Twitter" @img@@p@


#p#The Federal Government of Nigeria has finally lifted the country’s 7-month old Twitter ban. From the details of the agreement, the microblogging platform has agreed to some conditions which must be fulfilled before Q1 2022 ends. @p@
#p#Twitter has shown a willingness to register as a company in Nigeria, appoint a country representative to act as a liaison between the company and the Federal Government. In addition to enrolling Nigeria in its Partner Support and Law Enforcement Portals, the company has also agreed to applicable tax obligations on its operations under Nigerian law. @p@
#h3#Users’ reactions@h3@
#p#Since the announcement…@p@

#p#We are pleased that Twitter has been restored for everyone in Nigeria. Our mission in Nigeria & around the world, is to serve the public conversation. We are deeply committed to Nigeria, where Twitter is used by people for commerce, cultural engagement, and civic participation.@p@— Twitter Public Policy (@Policy) January 13, 2022

#p#… many Nigerians are happy about the development…@p@

#p#Feels great to be back here ❤️ #TwitterBan@p@— Cool DJ Jimmy Jatt (@djjimmyjatt) January 12, 2022


#p#Good to be back after suspension of #TwitterBan@p@— The Nation Nigeria (@TheNationNews) January 13, 2022

#p#…while others are either indifferent or sceptical. @p@

#p#I think Nigerians should keep using their VPNs.Make it harder for the government to trace you. Any government that can have this much power over service providers must also be doing a lot of electronic surveillance. Even GEJ tried the shit. Can't trust these ones more.@p@— Osaretin Victor Asemota (@asemota) January 13, 2022


#p#Nobody:Nigerians presenting their contents to lai mohammed before tweeting#TwitterBan pic.twitter.com/UwaRdoHw9F@p@— Dr. GHOST 👻 (@ghostperson01) January 13, 2022


#p#On lifting of #TwitterBan pic.twitter.com/F2CLDQ3xGF@p@— Amnesty International Nigeria (@AmnestyNigeria) January 12, 2022

#p#For all it’s worth, VPN companies might miss Nigerians…@p@

#p#People in Nigeria be like… #TwitterBan pic.twitter.com/e9wuHruBgj@p@— Windscribe (@windscribecom) January 13, 2022


#p##TwitterbanVPN companies to Nigerians right now: pic.twitter.com/ztLDEE7PJh@p@— Pulse Nigeria (@PulseNigeria247) January 12, 2022

#p#…or the other way round.@p@

#p#VPN farewell thread: Say goodbye to your VPN apps here 👇🏾 #TwitterBan@p@— Techpoint Africa (@Techpointdotng) January 13, 2022

#h3#Notes for concern@h3@
#p#While the implications of the ban are evident -— disruption of livelihoods, infringement on human rights, and other economic and social impacts — it remains to be seen who the losers and winners will be following this agreement. @p@

#TwitterBan update: Should you worry if Twitter succumbs to Nigerian government’s demands?

#p#It is, however, necessary to note that Twitter’s compliance could mean that it is obligated to take down tweets on authorities’ orders, divulge sensitive user information, or have its staff or executives punished if the company doesn’t comply with Nigerian laws.@p@
#p#This, invariably, will see the social media platform share the same fate as telcos and broadcasting outfits under the regulations of the Nigerian Communications Commission (NCC) and the National Broadcasting Commission (NBC). Going by recent cases, it is commonplace to find these organisations severely sanctioned for violating rules with grey areas. @p@
#p#Local telecommunications companies are unlikely to push back when orders clearly violating citizens’ fundamental right of access to information are given. Ordinarily, this does not apply to social media sites because they are not under their jurisdiction. @p@
#p#Even though it seems the company might be giving the government too much discretionary power, it chose to negotiate rather than go the litigation route, as was the case in India.@p@
#h4#A flawed precedent?@h4@
#p#If any other country has given Twitter a hard time, it’s India. The repression started early in 2021 when, on the premise of promoting free speech and privacy, Twitter restored the accounts of some journalists and media organisations that the government gave the order to deactivate or suspend. Asides from that, the company failed to comply with the country’s IT rules. In the months that followed, Twitter ran into more problems with the government, leading to the police visiting the company’s office in India to serve a notice.@p@
#p#By July, Twitter agreed to comply with all government conditions following a legal suit fully. The court directed Twitter to issue a statement saying it intends to abide by the rules. @p@
#p#India made a scapegoat of Twitter, which became an example for other Big Tech companies. As the government argued, Twitter has lost legal immunity for users’ posts in India. Could this be the Nigerian government’s plan? @p@
#p#If anything, strong-arming is common with governments that have shown authoritarian traits in the past and global company compliance might only fuel it.@p@
#h3#Far from over: Possible tales of ‘once again’@h3@
#p#While China is considered the region with the strictest Internet shutdowns, Africa is often regarded as the most volatile environment for social media. Sub-Saharan Africa’s history of Internet shutdowns dates back to 2007 with Guinea, and it was only a matter of time before other countries followed suit, with Nigeria joining the trend in 2020. @p@
#p#Currently, 32 of Africa’s 54 countries have restricted access to the Internet for similar reasons ranging from protests to strikes. Elections, national security, and examinations also present opportunities for restrictions. Specifically, shutdowns have proven to be one of the government’s tools to control information and communication.@p@
#p#It thus appears that a successful Internet shutdown in a country might result in many more. Ethiopia, for instance, has had 12 Internet shutdowns, and as of 2020, Chad had accumulated almost two and a half years of Internet disruptions within five years.@p@
#p#While circumventing social media censorship with VPNs appears to be the easiest way out, the issue of privacy and free speech are still cause for worry. Only time will tell if there will be more cases.@p@
#p#https://techpoint.africa/2021/02/26/sub-; there-africa-internet-shutdown-loses/@p@





#p#On January 22, 2022, be part of the largest gathering of innovators, startup founders, thinkers, programmers, policymakers, and investors in West Africa. Register free.@p@



 

"""
# print(virus.split('\n'))


try:
    print('Step 11111111')
    muyiwa = DisruptAfrica()
    print('Step 22222222')
    muyiwa.set_latest_post()
    print('Step 33333333')
    muyiwa.crawl_and_publish()
except:
    pass

try:
    print('Step 11111111')
    muyiwa = TechPoint()
    print('Step 22222222')
    muyiwa.set_latest_post()
    print('Step 33333333')
    muyiwa.crawl_and_publish()
except:
    pass

try:
    print('Step 11111111')
    muyiwa = TechCabal()
    print('Step 22222222')
    muyiwa.set_latest_post()
    print('Step 33333333')
    muyiwa.crawl_and_publish()
except:
    pass