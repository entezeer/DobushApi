from time import sleep
from . import parse_world, parse_kg
from .models import News
import celery
app = celery.Celery('example')

@app.task
def create_response():
    News.objects.all().delete()
    # parse_world.lenta()
    parse_world.mir24()
    parse_world.bbc()
    parse_kg.getNews()
    sleep(120)

# celery -A dobush worker -l info

