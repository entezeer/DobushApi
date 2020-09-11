from time import sleep

from celery import shared_task

from . import parse_world, parse_kg
from .models import News

@shared_task
def create_response():
    News.objects.all().delete()
    # parse_world.lenta()
    parse_world.mir24()
    parse_world.bbc()
    parse_kg.getNews()
    sleep(120)

# celery -A dobush worker -l info

