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

    def set_latest_post(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        raw_articles = soup.find_all('article', class_="article-list-item")
        x = 0
        stages = []
        for raw_article in raw_articles:
            print('Trying to curl page')
            url = raw_article.find('a', class_="article-list-title").attrs['href']
            a = raw_article.find('a', class_="article-list-category")
            if not a:
                continue
            category_link = a.attrs['href']
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
        stages.append(len(self.unvisited_latest))
        print(stages)

    def clean_empty_tags(self):
        super().clean_empty_tags()

    def secure_image(self, main_content):
        main_content = super().secure_image(main_content)
        main_content = main_content.replace('<li><a', '<a')  # to fix issue with li a img
        main_content = main_content.replace('</a></li>', '</a>')
        main_content = main_content.replace('<li class="blocks-gallery-item"><figure>',
                                            '<figure>')  # to fix issue with li a img
        main_content = main_content.replace('</figure>', '</figure>')  # to fix issue with li a img
        self.save_local_content(main_content)
        return main_content