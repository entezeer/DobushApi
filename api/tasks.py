from time import sleep

from celery import shared_task

from . import parse_world, parse_kg, parse_tech, parse_sports, parse_movie, parse_auto, parse_music


@shared_task
def create_request():
    sleep(60)
    parse_world.getNews()
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
