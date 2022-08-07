import requests
from bs4 import BeautifulSoup

from app.websites.blogger import Blogger


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

    def get_article_date(self):
        self.save_local_content(self.html_to_text)
        date = self.soup.find('span', class_='single-article-date')
        print(f'date = {date.text}')
        if date:
            date = date.text.replace(',', '').replace('th', '').replace('nd', '') \
                .replace('rd', '').replace('st', '').strip().lower().split(' ')
            formatted_date = f"{date[0]}-{self.month_dict[date[1][:3]]}-{date[2]}"
            return formatted_date
        return None

    def get_url(self):
        return 'https://techcabal.com/'

    def get_main_content(self, soup):
        main = soup.find('main')
        return main.contents[2]

    def get_main_content_terminator(self):
        return 'Share this article'

