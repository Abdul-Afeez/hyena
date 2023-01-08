import json

from flask import Flask, render_template, request
from playhouse.flask_utils import object_list

from app.consts.const import RAN, TECH_POINT_URL, QUEUED, QUILL_URL
from app.models.base import Job, WebMaster
from app.threads.mediator import Mediator, Inspector
from app.tools.parser import Parser

app = Flask(__name__, template_folder='template')


@app.route('/mediator')
def mediator():
    print('Mediator Initiating')
    mediate = Mediator()
    print('Mediator Initiated')
    mediate.run()
    return 'dONE'

@app.route('/inspector')
def inspector():
    print('Inspector Initiating')
    inspector = Inspector()
    print('Inspector Initiated')
    inspector.run()
    return 'dONE'

@app.route('/seed')
def seed():
    data = []
    for datum in data:
        try:
            job = Job()
            job.url = datum
            job.status = RAN
            job.save()
            print(f'Saving {job.url}')
        except Exception as e:
            print(e)
    return 'dONE'


@app.route('/test')
def test():
    out = json.dumps({
        "url": "https://techpoint.africa/",
        "h1": [["h1", "class", "lg:text-4xl", 0], "text"],
        "date": [["h5", "class", "mt-5 text-sm", 0], "text"],
        "date_engine": ["_january_01_1970", "last_finder"],
        "description": [["meta", "property", "og:description", 0], "content"],
        "main_content": [["div", "id", "article-content", 0], "tag"],
        "terminator": "@#*%[%[%",
        "unwanted_blocks": []
    })
    # print(out)
    # source =''
    # blogger = Parser()
    # data = blogger.extract(
    #     'https://disrupt-africa.com/2022/07/27/seedstars-announces-first-close-of-30m-emerging-market-seed-stage-fund/',
    #     source)
    # print(data)
    return 'dONE'


@app.route('/inspect/<job_id>', methods=('GET', 'POST'))
def inspect(job_id):
    job = Job.get(id=job_id)
    if request.method == 'POST':
        print(request.form)
        meta = {**job.meta, 'paraphrased_text': request.form['paraphrased_text'].replace('\n', '\n\n\n')}
        job.meta = meta
        job.status = request.form['status']
        job.save()
    paraphrased_text = job.meta.get('paraphrased_text', '').replace('\n\n\n', '\n') if job.meta else ''
    c_input = job.meta.get('c_input', '') if job.meta else ''
    data = {
        'c_input': c_input,
        'paraphrased_text': paraphrased_text,
        'job': job,
        'status': job.status
    }
    # print(data)

    return render_template('inspect.html', data=data)


@app.route('/jobs')
def jobs():
    query = []
    if request.args.get("id"):
        query.append(Job.id == request.args.get("id"))
    if request.args.get("status"):
        query.append(Job.status == request.args.get("status"))
    if request.args.get("date_from"):
        query.append(Job.last_updated >= request.args.get("date_from"))
    if request.args.get("date_to"):
        query.append(Job.last_updated <= request.args.get("date_to"))
    _jobs = Job.select()
    if len(query):
        print(tuple(query))
        _jobs = _jobs.where(tuple(query))
    _jobs = _jobs.order_by(Job.last_updated.desc())
    data = {
        'jobs': _jobs
    }
    print(len(_jobs))

    # return object_list('jobs.html', job)
    return render_template('jobs.html', jobs=_jobs)

    # return object_list(
    #     template_name='jobs.html',
    #     query=_jobs,
    #     context_variable='jobs',
    #     paginate_by=500)


@app.route('/create', methods=('GET', 'POST'))
def create():
    masters = WebMaster.filter(WebMaster.status == 'ACTIVE')
    if request.method == 'POST':
        print(request.form)
        job = Job()
        job.url = request.form['url']
        job.web_master_id = request.form['web_master_id']
        meta = {'url': job.url}
        job.meta = meta
        job.status = request.form['status']
        job.save()
    web_masters = []
    for web_master in masters:
        web_masters.append({"id": web_master.id, "name": web_master.name})
    return render_template('create.html', data={'web_masters': json.dumps(web_masters)})
