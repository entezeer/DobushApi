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
    News.objects.filter(category=Category.objects.get(name='Спорт')).filter(poll__isnull=True).all().delete()
    getChampionatNews()
    getSportsRuNews()


def getChampionatNews():
    response = requests.get('https://www.championat.com/articles/1.html', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('div.article-preview__info a.article-preview__subtitle[href]')[0:15]:
        try:
            response_ = requests.get('https://www.championat.com' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('div', class_='article-head__title').text

            try:
                images = soup.find('div', {"class": "article-head__photo"}).findChildren('img')
                for i in images:
                    img = i.get('src')
            except:
                img = None

            content = soup.select('div.article-content')[0]

            try:
                saveNews(title, str(content), 'https://www.championat.com' + a['href'], 'Championat.ru', img)
            except:
                print()

        except:
            print()

def getSportsRuNews():
    response = requests.get('https://www.sports.ru/news', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('a.short-text[href]')[0:10]:
        try:
            response_ = requests.get('https://www.sports.ru' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1', class_='h1_size_tiny').text

            content = soup.select('div.news-item__content')[0]

            try:
                saveNews(title, str(content), 'https://www.sports.ru' + a['href'], 'Sports.ru', None)

            except:
                print()
        except:
            print()

def saveNews(title, content, url, author, img):
    isExist = News.objects.filter(title=title).exists()
    if not isExist:
        News.objects.create(
            title=title,
            content=str(content),
            url=url,
            author=author,
            img=img,
            category=Category.objects.get(name='Спорт')
        )
