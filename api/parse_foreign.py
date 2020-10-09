import re
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
    News.objects.filter(category=Category.objects.get(name='Иностранные')).all().delete()
    getEuronewsNews()
    getCinHuaNews()
    getArabNews()
    getCnnNews()

def getArabNews():
    response = requests.get('https://www.alarabiya.net/latest-news', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    ar = bs.select('ul#Scroll li a[href]')[0:20]
    newAr = [v for k, v in enumerate(ar) if not k % 2]
    for a in newAr:
        try:
            response_ = requests.get('https://www.alarabiya.net' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1').text

            try:
                images = soup.find('div', {"class": "article-teaser"}).findChildren('img')
                for i in images:
                    img = i.get('src')
            except:
                img = None

            content = soup.select('div#body-text')[0]

            try:
                News.objects.create(
                    title=title,
                    content=str(content),
                    url='https://www.alarabiya.net' + a['href'],
                    author='www.alarabiya.net',
                    img=img,
                    category=Category.objects.get(name='Иностранные'),
                    language=3
                )
            except:
                print()

        except:
            print()

def getEuronewsNews():
    response = requests.get('https://www.euronews.com/news/international', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('div.o-block-more-news-themes__articles div.m-object__body h3 a')[0:10]:
        try:
            response_ = requests.get('https://www.euronews.com' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1', class_='c-article-title u-display-inline u-text-align--start').text

            try:
                img = soup.find('img', class_='c-article-media__img').get('src')
            except:
                img = None

            content = soup.select('div.c-article-content')
            try:
                News.objects.create(
                    title=title,
                    content=str(content),
                    url='https://www.euronews.com' + a['href'],
                    author='www.euronews.com',
                    img=img,
                    category=Category.objects.get(name='Иностранные'),
                    language=1
                )
            except:
                print()

        except:
            print()

def getCnnNews():
    response = requests.get('https://edition.cnn.com/world', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('h3.cd__headline a')[0:10]:
        try:
            response_ = requests.get('https://edition.cnn.com' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1', class_='pg-headline').text

            content = soup.select('div.l-container')

            try:
                News.objects.create(
                    title=title,
                    content=str(content),
                    url='https://edition.cnn.com' + a['href'],
                    author='edition.cnn.com',
                    img=None,
                    category=Category.objects.get(name='Иностранные'),
                    language=1
                )
            except:
                print()

        except:
            print()


def getCinHuaNews():
    response = requests.get('http://www.xinhuanet.com/world/', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('li.clearfix h3 a')[0:10]:
        try:
            print(a['href'])
            response_ = requests.get(a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('div', class_='h-title').text
            print(title)

            content = soup.select('div#p-detail')
            print(content)
            try:
                News.objects.create(
                    title=title,
                    content=str(content),
                    url=a['href'],
                    author='www.xinhuanet.com',
                    img=None,
                    category=Category.objects.get(name='Иностранные'),
                    language=2
                )
            except:
                print()

        except:
            print()

def getWorldJournalNews():
    response = requests.get('https://www.worldjournal.com/wj/cate/breaking',
                            headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    ar = bs.select('div.subcate-list__link__text a[href]')[0:20]
    newAr = [v for k, v in enumerate(ar) if k % 2]
    for a in newAr:
        try:
            response_ = requests.get(a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1', class_='article-content__title').text

            content = soup.select('section.article-content__editor')

            try:
                News.objects.create(
                    title=title,
                    content=str(content),
                    url=a['href'],
                    author='www.worldjournal.com',
                    img=None,
                    category=Category.objects.get(name='Иностранные'),
                    language=2
                )
            except:
                print()

        except:
            print()