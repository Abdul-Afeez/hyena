from bs4 import Tag, NavigableString, BeautifulSoup

from app.models.base import WebMaster
from app.tools.blogger import Blogger

config = [
    {
        "url": "https://techcabal.com/",
        "h1": [
            [
                "h1",
                "class",
                "single-article-title",
                "0"
            ],
            "text"
        ],
        "date": [
            [
                "span",
                "class",
                "single-article-date",
                "0"
            ],
            "text"
        ],
        "date_engine": [
            "_01st_january_1970"
        ],
        "description": [
            [
                "meta",
                "property",
                "og:description",
                "0"
            ],
            "content"
        ],
        "main_content": [
            [
                "main",
                "",
                "",
                2
            ],
            "contents"
        ],
        "terminator": "Share this article",
        "unwanted_blocks": [
            [
                [
                    "div",
                    "class",
                    "single-article-info",
                    "0"
                ],
                "tag",
                True
            ],
            [
                [
                    "div",
                    "class",
                    "single-article-category",
                    "0"
                ],
                "tag",
                True
            ],
            [
                [
                    "div",
                    "class",
                    "list-newsletter-form shortcode",
                    "0"
                ],
                "tag",
                True
            ]
        ],
        "bad_signature": [[["div", "class", "single-article-category", "0"], "text", "newsletter"]]
    }
]


class Parser(Blogger):

    def __init__(self, config):
        super().__init__()

        self.config = config

    def get_h1(self):
        return self.find(self.config.get('h1'))

    def get_article_date(self):
        raw_date = self.find(self.config.get('date'))
        engines = self.config.get('date_engine')
        date_finder = DateFinder(raw_date, engines)
        date = date_finder.run()
        print(f'Programmable date ==== {date}')
        return date

    def get_description(self, soup):
        print(self.config.get('description'))
        print('Before')
        return self.find(self.config.get('description'))

    def get_main_content(self, soup):
        return self.find(self.config.get('main_content'))

    def remove_unwanted_blocks(self, soup):
        unwanted_blocks = self.config.get('unwanted_blocks', [])
        for unwanted_block in unwanted_blocks:
            try:
                cow_dungs = self.find(unwanted_block)
                for cow_dung in cow_dungs:
                    if isinstance(cow_dung, NavigableString):
                        continue
                    else:
                        cow_dung.decompose()
            except Exception as e:
                print(e)
        return soup

    def get_main_content_terminator(self):
        return self.config.get('terminator')


class DateFinder:
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

    def __init__(self, raw_date, engines):
        self.raw_date = raw_date
        self.date = None
        self.engines = engines

    def _january_01_1970(self):
        try:
            print('Trying first')
            raw_date = self.raw_date.split('<!')[0].replace(',', '').replace('"', '').strip().lower().split(' ')
            print('Date now = ', raw_date)
            formatted_date = f"{raw_date[1]}-{self.month_dict[f'{raw_date[0]}'[:3]]}-{raw_date[2]}"
            self.date = formatted_date
        except Exception as e:
            print(f'Date not found None')
            print(e)

    def last_finder(self):
        print('Resolving to alternative date finder')
        print('Date now = ', self.raw_date)
        try:
            print('Trying second')
            broken_date = self.raw_date.split('T')[0].split('-')
            formatted_date = f'{broken_date[2]}-{broken_date[1]}-{broken_date[0]}'
            self.date = formatted_date
        except Exception as e:
            print(e)

    def _01st_january_1970(self):
        try:
            date = self.raw_date.replace(',', '').replace('th', '').replace('nd', '') \
                .replace('rd', '').replace('st', '').strip().lower().split(' ')
            formatted_date = f"{date[0]}-{self.month_dict[date[1][:3]]}-{date[2]}"
            self.date = formatted_date
        except Exception as e:
            print(e)

    def confirm_date(self):
        try:
            return len(self.date.split('-')) == 3
        except Exception as e:
            return False

    def get_engines(self):
        return {
            '_january_01_1970': self._january_01_1970,
            'last_finder': self.last_finder,
            '_01st_january_1970': self._01st_january_1970,
        }

    def run(self):
        all_engines = self.get_engines()
        print('self.engines', self.engines)
        for engine in self.engines:
            date_finder = all_engines[engine]
            date_finder()
            print('self.date ==== ', self.date)
            if self.confirm_date():
                break
        if self.confirm_date():
            return self.date
        return None
