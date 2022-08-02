import datetime
import json

from peewee import Model, TextField, CharField, DateTimeField, AutoField, MySQLDatabase

try:
    database = MySQLDatabase('hyena', user='hyena_engine_user', password='*121*HYEna#',
                             host='db', port=3306)
    database.connect()
except Exception as e:
    database = MySQLDatabase('hyena', user='hyena_engine_user', password='*121*HYEna#',
                             host='localhost', port=3306)
    database.connect()


class JSONField(TextField):

    def __init__(self, **kwargs):
        super().__init__(kwargs)

    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        if value is not None:
            return json.loads(value)


class DBConnect:
    handle = None

    def __init__(self):
        if not DBConnect.handle:
            database.connect()
            DBConnect.handle = True
            database.create_tables([Job])


class BaseModel(Model):
    class Meta:
        database = database


class Job(BaseModel):
    id = AutoField()
    link = CharField(max_length=800)
    url = CharField(max_length=800)
    status = CharField(null=True)
    sub_status = CharField(null=True)
    meta = JSONField(default={}, max_length=8000000)
    created_date = DateTimeField(default=datetime.datetime.now)
    last_updated = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.last_updated = datetime.datetime.now()
        return super(Job, self).save(*args, **kwargs)
