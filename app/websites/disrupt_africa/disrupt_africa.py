import re

import requests
from bs4 import BeautifulSoup

from app.websites.blogger import Blogger


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

    def get_article_date(self):
        date = self.soup.find('time', class_='value-title')
        if date:
            date = date.text.replace(',', '').strip().lower().split(' ')
            formatted_date = f"{date[1]}-{self.month_dict[date[0][:3]]}-{date[2]}"
            return formatted_date
        return None

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
        # self.save_local_content(soup, '')
        print('000000000000000')
        raw_articles = soup.find('ul', class_="wpp-list wpp-cards").find_all('li')
        stages = []
        for raw_article in raw_articles:
            a = raw_article.find('a')
            url = a.attrs['href']
            crawled = self.confirm_page_crawled(url)
            if not crawled:
                self.unvisited_latest.append(url)
        stages.append(len(self.unvisited_latest))
        print('000000000000000')
        raw_articles = soup.find_all('a', class_='title')
        for raw_article in raw_articles:
            url = raw_article.attrs['href']
            crawled = self.confirm_page_crawled(url)
            if not crawled:
                self.unvisited_latest.append(url)
        stages.append(len(self.unvisited_latest))

        cow_dungs = soup.find_all('span', class_='cat cat-title cat-38')
        for cow_dung in cow_dungs:
            cow_dung.decompose()
        stages.append(len(self.unvisited_latest))

        raw_articles = soup.find_all('article')
        for raw_article in raw_articles:
            a = raw_article.find('a')
            url = a.attrs['href']
            if 'category' in url:
                continue
            crawled = self.confirm_page_crawled(url)
            if not crawled:
                self.unvisited_latest.append(url)
        stages.append(len(self.unvisited_latest))
        print(stages)

    def clean_empty_tags(self):
        super().clean_empty_tags()
