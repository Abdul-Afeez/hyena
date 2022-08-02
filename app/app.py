from flask import Flask, render_template, request
from playhouse.flask_utils import object_list

from app.consts.const import RAN, TECH_POINT_URL, QUEUED, QUILL_URL
from app.models.base import Job
from app.threads.mediator import Mediator

app = Flask(__name__, template_folder='template')



@app.route('/mediator')
def mediator():
    print('Mediator Initiating')
    mediate = Mediator()
    print('Mediator Initiated')
    mediate.run()
    return 'dONE'


@app.route('/job-filter')
def test():
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

@app.route('/techpoint')
def techpoint():
    print('Crawling techpoint')
    job = Job()
    job.url = TECH_POINT_URL
    job.status = QUEUED
    job.link = TECH_POINT_URL
    job.meta = {'url': TECH_POINT_URL, 'maximum': 10000}
    job.save()
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
    print(data)

    return render_template('inspect.html', data=data)


@app.route('/jobs')
def jobs():
    query = []
    if request.args.get("id"):
        query.append(Job.id == request.args.get("id"))
    if request.args.get("status"):
        query.append(Job.status == request.args.get("status"))
    if request.args.get("link") and request.args.get("link") == 'paraphrase':
        query.append(Job.link == QUILL_URL)
    if request.args.get("link") and request.args.get("link") == 'tech_point':
        query.append(Job.link == f'{TECH_POINT_URL}')
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
    # print(len(_jobs))

    # return object_list('jobs.html', job)
    # return render_template('jobs.html', jobs=_jobs)

    return object_list(
        template_name='jobs.html',
        query=_jobs,
        context_variable='jobs',
        paginate_by=500)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        print(request.form)
        job = Job()
        Job.url = request.form['url']
        Job.link = request.form['link']
        meta = {'url': Job.url}
        job.meta = meta
        job.status = request.form['status']
        job.save()

    return render_template('create.html', data={})
