import re
from app.websites.blogger import Blogger


class DisruptAfricaParser(Blogger):
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
