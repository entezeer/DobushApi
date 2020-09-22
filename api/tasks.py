from celery import Celery
from celery.task import periodic_task
from datetime import timedelta
from os import environ
from time import sleep

from . import parse_world, parse_kg
from .models import News
import celery

app = celery.Celery('dobush')

REDIS_URL = environ.get('REDISTOGO_URL', 'redis://localhost')

# Use Redis as our broker and define json as the default serializer
celery = Celery('tasks', broker=REDIS_URL)


@periodic_task(run_every=timedelta(minutes=3))
def create_request():
    News.objects.all().delete()
    # parse_world.lenta()
    parse_world.mir24()
    parse_world.bbc()
    parse_kg.getNews()
    # sleep(3600)

# while True:
#     create_response()
# celery -A dobush worker -l info
