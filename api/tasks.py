from time import sleep

from celery import shared_task

from . import parse_world, parse_kg, parse_tech, parse_sports, parse_movie, parse_auto, parse_music
from .models import News


@shared_task
def create_request():
    News.objects.all().delete()
    # parse_world.lenta()
    parse_world.mir24()
    parse_world.bbc()
    parse_kg.getNews()
    parse_sports.getNews()
    parse_tech.getNews()
    parse_auto.getNews()
    parse_music.getNews()
    parse_movie.getNews()
    sleep(3600)


while True:
    create_request()
# celery -A dobush worker -l info
