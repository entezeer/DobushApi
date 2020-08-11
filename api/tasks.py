from time import sleep
from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

from . import parse_world, parse_kg
from .models import News


# celery -A dobush worker -l info
@shared_task
# some heavy stuff here
def create_response():
    News.objects.all().delete()
    # parse_world.lenta()
    parse_world.mir24()
    parse_world.bbc()
    parse_kg.getNews()

@shared_task
# some heavy stuff here
def update_db():
    print('Updating data ..')

    # Currency.objects.all().delete()


    sleep(2)


create_response()
while True:
    sleep(60)
    # update_currency()
