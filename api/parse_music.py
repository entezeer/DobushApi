from bs4 import BeautifulSoup
from pip._vendor import requests

from .models import News, Category

headers = {
    'authority': 'www.kith.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
}
session = requests.session()

def getNews():
    News.objects.filter(category=Category.objects.get(name='Музыка')).all().delete()
    getMusicNews()

def getMusicNews():
    response = session.get('https://rg.ru/tema/kultura/music/pop/', headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    for a in bs.select('h2.b-news-inner__list-item-title a[href]')[0:5]:
        try:
            response_ = session.get('https://rg.ru' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.text, 'lxml')
            try:
                img = soup.find('img', class_='b-material-img__img').get('src')
            except:
                img = None

            title = soup.find('h1', class_='b-material-head__title').get_text()

            content = soup.select('div.b-material-wrapper__text')[0]

            try:
                News.objects.create(
                    title=title,
                    content=str(content),
                    url='https://rg.ru' + a['href'],
                    author='rg.ru',
                    img=img,
                    category=Category.objects.get(name='Музыка')
                )
            except:
                print()

        except:
            print()