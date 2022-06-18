
from flask import Flask

from app.websites.disrupt_africa.disrupt_africa import DisruptAfrica
from app.websites.techcabal.techcabal import TechCabal
from app.websites.techpoint.techpoint import TechPoint

app = Flask(__name__)


@app.route('/disrupt-africa')
def disrupt_africa():
    try:
        print('Step 11111111')
        muyiwa = DisruptAfrica()
        print('Step 22222222')
        muyiwa.set_latest_post()
        print('Step 33333333')
        muyiwa.crawl_and_publish()
    except Exception as e:
        print(e)
        pass
    return 'Done'


@app.route('/tech-point')
def tech_point():
    try:
        print('Step 11111111')
        muyiwa = TechPoint()
        print('Step 22222222')
        muyiwa.set_latest_post()
        print('Step 33333333')
        muyiwa.crawl_and_publish()
    except Exception as e:
        print(e)
        pass
    return 'Done'


@app.route('/tech-cabal')
def tech_cabal():
    try:
        print('Step 11111111')
        muyiwa = TechCabal()
        print('Step 22222222')
        muyiwa.set_latest_post()
        print('Step 33333333')
        muyiwa.crawl_and_publish()
    except Exception as e:
        print(e)
        pass
    return 'Done'


@app.route('/every')
def every():
    disrupt_africa()
    tech_cabal()
    tech_point()