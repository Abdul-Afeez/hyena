from app.websites.blogger import Blogger
from app.websites.techpoint.techpoint_browser import TechPointBrowser


class TechPoint(Blogger):

    def __init__(self):
        super().__init__()
        self.name = 'Techpoint'

    def get_url(self):
        return 'https://techpoint.africa/'

    def get_h1_class(self):
        return 'lg:text-4xl'

    def get_article_date(self):
        date = self.soup.find('h5', class_='mt-5 text-sm')
        if date:
            date = date.text.split('<!')[0].replace(',', '').strip().lower().split(' ')
            # print('date = ', date)
            formatted_date = f"{date[1]}-{self.month_dict[f'{date[0]}'[:3]]}-{date[2]}"
            return formatted_date
        return None

    def get_description(self, soup):
        return soup.find('meta', property="og:description").attrs['content']

    def get_main_content(self, soup):
        main = soup.find('div', id='article-content')
        return main.contents[0]

    def remove_unwanted_blocks(self, soup):
        return soup

    def get_main_content_terminator(self):
        return '@#*%(%(%'

    def terminate(self, terminator=None):
        super().terminate()

    def set_latest_post(self):
        tech_point_browser = TechPointBrowser()
        tech_point_browser.set_browser(self.url)
        raw_links = tech_point_browser.crawl(50)
        self.unvisited_latest = list(set(raw_links))
        self.save_local_content(raw_links, '-techpoint-urls')
        # self.unvisited_latest = ['https://techpoint.africa/2022/02/08/why-are-artistes-interested-in-african-startups']
