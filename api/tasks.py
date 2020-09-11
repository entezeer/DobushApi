from time import sleep

from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task

from . import parse_world, parse_kg
from .models import News

@periodic_task(run_every=crontab(minute=60))
def create_response():
    News.objects.all().delete()
    # parse_world.lenta()
    parse_world.mir24()
    parse_world.bbc()
    parse_kg.getNews()
    sleep(3600)


create_response()
# celery -A dobush worker -l info
