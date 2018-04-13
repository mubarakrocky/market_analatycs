from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab

class Config:
    broker = 'amqp://guest@localhost//'
    enable_utc = True
    timezone = 'Europe/London'
    imports = ('pull_data_from_yahoo')
    beat_schedule = {
        'pull_data':{
            'task':'pull_data_from_yahoo.pull_data_from_yahoo',
            'schedule':crontab('*/1'),
        },
    }

app = Celery('trading')
app.config_from_object(Config)
