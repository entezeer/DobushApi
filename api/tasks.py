from datetime import timedelta
from os import environ
from time import sleep

from . import parse_world, parse_kg
from .models import News
import celery
app = celery.Celery('dobush')

REDIS_URL = environ.get('REDISTOGO_URL', 'redis://localhost')

# Use Redis as our broker and define json as the default serializer
app.conf.update(
    BROKER_URL=REDIS_URL,
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERYBEAT_SCHEDULE = {
        'get_news': {
            'task': 'tasks.create_request',
            'schedule': timedelta(minutes=2)
        },
    }
)

@celery.task
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
