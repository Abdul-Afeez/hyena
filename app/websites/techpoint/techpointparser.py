from bs4 import BeautifulSoup

from app.consts.const import TECH_POINT_URL
from app.websites.blogger import Blogger


class TechPointParser(Blogger):

    def __init__(self):
        super().__init__()
        self.name = 'Techpoint'

    def get_url(self):
        return TECH_POINT_URL

    def get_h1_class(self):
        return 'lg:text-4xl'

    def get_article_date(self):
        date = self.soup.find('h5', class_='mt-5 text-sm')
        print(f'Date: {date}')
        if date:
            try:
                print('Trying first')
                date = date.text.split('<!')[0].replace(',', '').replace('"', '').strip().lower().split(' ')
                print('Date now = ', date)
                formatted_date = f"{date[1]}-{self.month_dict[f'{date[0]}'[:3]]}-{date[2]}"
                return formatted_date
            except Exception as e:
                print(f'Date not found None')
                print(e)
        else:
            print('Resolving to alternative date finder')
            date = self.soup.find('time').attrs['datetime']  #  2021-06-05T18:14:51.000Z
            if date:
                print('Date now = ', date)
                try:
                    print('Trying second')
                    broken_date = date.split('T')[0].split('-')
                    formatted_date = f'{broken_date[2]}-{broken_date[1]}-{broken_date[0]}'
                    return formatted_date
                except Exception as e:
                    print(e)
        return None

    def get_description(self, soup):
        description_text = soup.find('meta', property="og:description").attrs['content']
        print(f'Techpoint Description Text === {description_text}')
        return description_text

    def get_main_content(self, soup):
        main = soup.find('div', id='article-content')
        return main.contents[0]

    def remove_unwanted_blocks(self, soup):
        return soup

    def get_main_content_terminator(self):
        return '@#*%(%(%'

    def terminate(self, terminator=None):
        super().terminate()
