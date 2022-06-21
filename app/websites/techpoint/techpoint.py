from bs4 import BeautifulSoup

from app.websites.blogger import Blogger
from app.websites.spider import Spider
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
        print(f'Date: {date}')
        if date:
            try:
                date = date.text.split('<!')[0].replace(',', '').replace('"', '').strip().lower().split(' ')
                print('Date now = ', date)
                formatted_date = f"{date[1]}-{self.month_dict[f'{date[0]}'[:3]]}-{date[2]}"
                print(f'Date not found None')
                return formatted_date
            except Exception as e:
                print(e)

        else:
            print('Resolving to alternative date finder')
            date = self.soup.find('time').attrs['datetime']  #  2021-06-05T18:14:51.000Z
            if date:
                print('Date now = ', date)
                try:
                    broken_date = date.split('T')[0].split('-')
                    formatted_date = f'{broken_date[2]}-{broken_date[1]}-{broken_date[0]}'
                    return formatted_date
                except Exception as e:
                    print(e)
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
        # tech_point_browser = TechPointBrowser()
        # tech_point_browser.set_browser(self.url)
        # raw_links = tech_point_browser.crawl(200)
        # self.unvisited_latest = list(set(raw_links))
        # self.save_content(raw_links, '-techpoint-urls', 'tech-point-urls')
        # to be recrawled ['']
        self.unvisited_latest = ['https://techpoint.africa/2021/04/15/udux-piggyvest-partnership-poprev', 'https://techpoint.africa/2021/11/23/thepeer-lets-businesses-share-data', 'https://techpoint.africa/2021/11/16/meme-coins-and-wakanda-inu', 'https://techpoint.africa/2021/10/01/twitterban-update-october-first', 'https://techpoint.africa/2021/08/05/mvx-1-3m-funding', 'https://techpoint.africa/2021/07/08/kenyan-b2b-marketforce-2m-pre-seriesa', 'https://techpoint.africa/2021/11/18/the-next-frontier-edtech', 'https://techpoint.africa/2021/06/22/nithio-fi-investment-from-fsd-africa', 'https://techpoint.africa/2021/04/14/numida-raises-2-3m-mtns-mobile-money-valuation-linkedin-new-job-titles', 'https://techpoint.africa/2021/08/30/international-day-disappeared', 'https://techpoint.africa/2021/10/01/nigerias-proposed-startup-bill', 'https://techpoint.africa/2021/03/18/nigerian-digital-bank-kuda-secures-25m-series-a-four-months-after-raising-10m-seed', 'https://techpoint.africa/2021/12/31/memorable-moments-for-african-tech', 'https://techpoint.africa/2021/07/02/fairmoney-raises-42m-seriesb', 'https://techpoint.africa/2021/06/29/cowrywise-secures-secs-licence', 'https://techpoint.africa/2021/05/11/facebook-clubhouse-live-audio', 'https://techpoint.africa/2021/05/11/maviance-3-million-funding-2', 'https://techpoint.africa/2021/09/08/improving-literacy-phones-tech-tools', 'https://techpoint.africa/2021/11/17/kredi-bank-financial-services', 'https://techpoint.africa/2021/11/23/uk-based-tech-company-with-a-presence-in-nigeriatorilo-launches-all-in-one-productivity-tool-bizedge', 'https://techpoint.africa/2021/06/30/81-smes-optimistic', 'https://techpoint.africa/2021/05/11/building-from-groundup-jessica-hope', 'https://techpoint.africa/2021/03/30/curacel-450k-pre-seed-raise', 'https://techpoint.africa/2021/04/01/private-companies-nin', 'https://techpoint.africa/2021/06/23/tech-big-5-collapse', 'https://techpoint.africa/2021/08/27/6-ways-to-spice-up-youtube-shorts', 'https://techpoint.africa/2021/05/12/insight-from-africa-product-management-report', 'https://techpoint.africa/2021/07/07/inec-pvc-online-registration', 'https://techpoint.africa/2021/06/04/nigeria-suspends-twitter', 'https://techpoint.africa/2021/05/18/increase-in-safaricoms-internet-data-revenue', 'https://techpoint.africa/2021/09/28/universal-access-information-day-2021', 'https://techpoint.africa/2021/08/04/rachael-akalia-patricia', 'https://techpoint.africa/2021/05/27/cbn-licence-fintech', 'https://techpoint.africa/2021/04/15/you-can-now-buy-and-register-new-sims-in-nigeria-from-april-19-2021', 'https://techpoint.africa/2021/05/14/nigerian-blockchain-hub-abuja', 'https://techpoint.africa/2021/06/28/jiji-reportedly-acquires-cars45', 'https://techpoint.africa/2021/07/17/emoji-day-digital-language', 'https://techpoint.africa/2021/08/09/3-reasons-not-to-miss-sme-clinic-2021', 'https://techpoint.africa/2021/05/13/airtel-q1-2021-financial-report', 'https://techpoint.africa/2021/04/14/nigerias-gig-logistics-uk-launch', 'https://techpoint.africa/2021/12/20/the-next-frontier-for-music', 'https://techpoint.africa/2021/07/15/technology-employment-entrepreneurship', 'https://techpoint.africa/2021/11/22/nitda-partners-fccpc', 'https://techpoint.africa/2021/12/17/zimbabwe-data-protection-act', 'https://techpoint.africa/2021/05/10/clubhouse-android-launch', 'https://techpoint.africa/2021/08/05/flutterwave-us-expansion', 'https://techpoint.africa/2021/05/31/youtube-terms-of-service-update', 'https://techpoint.africa/2021/06/22/ecowas-court-twitter-ban', 'https://techpoint.africa/2021/06/23/sec-chaka-broker-licence', 'https://techpoint.africa/2021/08/03/khula-seed-raise', 'https://techpoint.africa/2021/09/02/bumpa-digitise-thousands-businesses', 'https://techpoint.africa/2021/07/07/daystar-power-funding', 'https://techpoint.africa/2021/10/05/edtech-innovations-in-africa', 'https://techpoint.africa/2021/07/05/egyptian-ecommerce-maxab-40m', 'https://techpoint.africa/2021/07/02/twitter-ban-reps-silent', 'https://techpoint.africa/2021/07/30/system-admin-appreciation-day', 'https://techpoint.africa/2021/06/07/twitterban-vpns-nigerians', 'https://techpoint.africa/2021/09/21/zola-electric-energy-in-africa', 'https://techpoint.africa/2021/09/13/hardware-convention-review', 'https://techpoint.africa/2021/07/08/smile-identity-funding', 'https://techpoint.africa/2021/08/02/what-to-expect-at-sme-clinic-2021', 'https://techpoint.africa/2021/04/12/twitter-ghana-office', 'https://techpoint.africa/2021/06/21/register-small-business-cac-online', 'https://techpoint.africa/2021/07/30/airtel-africa-200-million', 'https://techpoint.africa/2021/07/01/facebook-google-tiktok-twitter-commit', 'https://techpoint.africa/2022/02/08/why-are-artistes-interested-in-african-startups', 'https://techpoint.africa/2021/07/07/lidya-raises-pre-series-b', 'https://techpoint.africa/2021/05/11/maviance-3-million-funding', 'https://techpoint.africa/2021/05/10/uber-increase-price-lagos', 'https://techpoint.africa/2021/08/02/catalyst-fund-new-cohort', 'https://techpoint.africa/2022/01/19/techpoint-build-spotlight-bitmama', 'https://techpoint.africa/2021/05/17/telda-5-million-pre-seed', 'https://techpoint.africa/2021/09/14/crypto-and-cbdc', 'https://techpoint.africa/2022/01/06/nigerian-fintech-predictions-2022', 'https://techpoint.africa/2022/03/25/quidax-unveils-don-jazzy-as-its-brand-ambassador', 'https://techpoint.africa/2021/09/22/afcfta-nigeria-ip', 'https://techpoint.africa/2021/10/01/cbn-postpones-enaira-launch', 'https://techpoint.africa/2021/12/17/help-ambulance-services', 'https://techpoint.africa/2021/10/04/bitmama-raises-pre-seed', 'https://techpoint.africa/2021/07/05/convert-instagram-followers-paying-customers', 'https://techpoint.africa/2021/06/01/talentql-pipeline-senior-engineers', 'https://techpoint.africa/2021/12/15/nestcoins-metaverse-magna', 'https://techpoint.africa/2021/06/07/twitter-ban-legal', 'https://techpoint.africa/2021/03/23/vesicash-escrow-services', 'https://techpoint.africa/2021/07/02/payhippo-1m-pre-seed', 'https://techpoint.africa/2021/03/22/blueloop-y-combinator-w21', 'https://techpoint.africa/2021/05/31/chipper-cash-raises-100m', 'https://techpoint.africa/2021/09/13/world-suicide-prevention-day', 'https://techpoint.africa/2021/04/14/nigerian-government-launch-eye-mark', 'https://techpoint.africa/2022/01/13/nigeria-lifts-twitter-ban', 'https://techpoint.africa/2021/09/21/techpoint-build-2021', 'https://techpoint.africa/2021/08/10/jumia-and-national-bank-of-egypt', 'https://techpoint.africa/2021/06/07/improve-small-business-tech', 'https://techpoint.africa/2021/11/23/mr-eazi-empawa-africa', 'https://techpoint.africa/2021/06/24/learning-disabilities-assistive-technology', 'https://techpoint.africa/2021/03/17/gokada-new-ceo-nikhil-goel', 'https://techpoint.africa/2021/07/05/facebook-partnership-fibre-network']
        # ['https://techpoint.africa/2022/02/01/indicina-ethical-loan-recovery', 'https://techpoint.africa/2021/10/12/sudans-first-investment-in-years', 'https://techpoint.africa/2022/06/17/amber-group-now-licensed-to-operate-in-hong-kong-with-acquisition-of-celera-markets-limited', 'https://techpoint.africa/2021/10/06/subsea-internet-cable-google-africa', 'https://techpoint.africa/2022/03/23/ukraine-legalises-crypto', 'https://techpoint.africa/2021/12/13/world-toilet-day', 'https://techpoint.africa/2021/09/29/how-tekedia-capital-invests', 'https://techpoint.africa/2022/01/13/y-combinator-500k-deal', 'https://techpoint.africa/2022/01/18/orda-1-1m-funding', 'https://techpoint.africa/2021/11/12/technext-coinference-2021', 'https://techpoint.africa/2022/03/24/tingo-a-nigerian-tech-company-is-attempting-to-dominate-the-fintech-market-after-making-inroads-into-agribusiness', 'https://techpoint.africa/2021/09/15/africa-and-the-global-edtech-industry', 'https://techpoint.africa/2021/09/07/vahlid-escrow-service-provid', 'https://techpoint.africa/2022/01/28/crypto-beyond-trading-build-2021', 'https://techpoint.africa/2022/03/25/quidax-unveils-don-jazzy-as-its-brand-ambassador', 'https://techpoint.africa/2021/09/07/south-africa-5g-shaky', 'https://techpoint.africa/2021/10/12/healthtracka-digital-diagnostics', 'https://techpoint.africa/2021/10/19/healthtracka-techstars-toronto', 'https://techpoint.africa/2022/03/09/okhi-raises-1-5million', 'https://techpoint.africa/2022/01/17/how-wiicreate-is-helping-african-startups-improve-brand-visibility-with-branded-merchandise', 'https://techpoint.africa/2021/10/15/paysika-350k-preseed', 'https://techpoint.africa/2022/06/17/nigerias-kannywood-streaming-platform-northflix-clocks-three-years-spread-to-over-85-countries', 'https://techpoint.africa/2022/03/25/hytch-ride-sharing-hitchhiking']

    def get_page(self, url):
        self.spider.set_browser(url)
        content = self.spider.get_page_content()
        return BeautifulSoup(content, "html.parser")

