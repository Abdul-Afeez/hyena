import datetime
import json

from peewee import Model, TextField, CharField, DateTimeField, AutoField, MySQLDatabase, IntegerField, ForeignKeyField, \
    PrimaryKeyField

from app.indexed_search.indexed_search import Indexer, ComparativeScorer, JITIndexer

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
        # print(value)
        return json.dumps(value)

    def python_value(self, value):
        try:
            if value is not None:
                return json.loads(value)
        except Exception as err:
            # print('##################################Possible culprit###############################')
            # print('#################################################################################')
            # print('#################################################################################')
            # print('#################################################################################')
            # print(value)
            # print('**********************************************************************************')
            # print('**********************************************************************************')
            # print('**********************************************************************************')
            # print('**********************************************************************************')
            # print(err)
            # print('**********************************************************************************')
            # print('**********************************************************************************')
            # print('**********************************************************************************')
            # print('**********************************************************************************')
            return {}


class BaseModel(Model):
    class Meta:
        database = database


class WebMaster(BaseModel):
    id = PrimaryKeyField()
    name = CharField(max_length=800)
    url = CharField(max_length=800, default='Webmaster')
    max_session = IntegerField(default=1)
    delay = IntegerField(default=3)
    status = CharField(null=True)
    reconnaissance = JSONField(default={}, max_length=80000)
    parser = JSONField(default={}, max_length=80000)
    created_date = DateTimeField(default=datetime.datetime.now)
    last_updated = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.last_updated = datetime.datetime.now()
        return super(WebMaster, self).save(*args, **kwargs)


class Job(BaseModel):
    id = PrimaryKeyField()
    web_master_id = ForeignKeyField(WebMaster, to_field="id")
    url = CharField(max_length=800)
    reference_url = CharField(max_length=800, null=True)
    jit_score = CharField(max_length=800, null=True)
    status = CharField(null=True)
    sub_status = CharField(null=True)
    meta = JSONField(default={}, max_length=8000000)
    created_date = DateTimeField(default=datetime.datetime.now)
    last_updated = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.last_updated = datetime.datetime.now()
        return super(Job, self).save(*args, **kwargs)


class Index(BaseModel):
    id = PrimaryKeyField()
    token = CharField(max_length=800)
    shard = JSONField(max_length=80000000)
    status = CharField(null=True)
    total = IntegerField(null=True)
    meta = JSONField(default={}, max_length=80000000)
    created_date = DateTimeField(default=datetime.datetime.now)
    last_updated = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.last_updated = datetime.datetime.now()
        return super(Index, self).save(*args, **kwargs)



class DBConnect:
    handle = None

    def __init__(self):
        if not DBConnect.handle:
            DBConnect.handle = True
            # database.create_tables([Job, WebMaster, Index])
# DBConnect()
