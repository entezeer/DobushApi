from time import sleep

from celery import shared_task

from . import parse_world, parse_kg, parse_tech, parse_sports, parse_movie, parse_auto, parse_music, parse_foreign, update_dynos


@shared_task
def create_request():
    parse_world.getNews()
    parse_kg.getNews()
    parse_sports.getNews()
    parse_tech.getNews()
    parse_auto.getNews()
    parse_music.getNews()
    parse_movie.getNews()
    parse_foreign.getNews()
    sleep(3300)

while True:
    create_request()
# celery -A dobush worker -l info
