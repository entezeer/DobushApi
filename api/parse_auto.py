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
    getAdtNews()
    getAutoNews()


def getAdtNews():
    response = requests.get('https://adt.by/cat/mirovye-avtonovosti', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('h3.elementor-post__title a[href]')[0:10]:
        try:
            response_ = requests.get(a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1', class_='post-title single-post-title entry-title').text

            try:
                image = soup.find('span', {
                    "class": "attachment-penci-full-thumb size-penci-full-thumb penci-single-featured-img wp-post-image penci-disable-lazy"})[
                    'style']
                image_ = re.search("https.*[)]", image)
                img = image[image_.start():image_.end() - 1]
            except:
                img = None

            content = soup.select('div#penci-post-entry-inner')[0]

            try:
                News.objects.create(
                    title=title,
                    content=str(content),
                    url=a['href'],
                    author='adt.by',
                    img=img,
                    category=Category.objects.get(name='Авто')
                )
            except:
                print()

        except:
            print()


def getAutoNews():
    response = requests.get('https://www.autonews.ru/tags/?tag=%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8',
                            headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('a.item-big__link[href]')[0:5]:
        try:
            response_ = requests.get(a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1', class_='js-slide-title').text

            try:
                images = soup.find('div', {"class": "article__main-image__image"}).findChildren('img')
                for i in images:
                    img = i.get('src')
            except:
                img = None

            content = soup.select('div.article__text')[0]

            try:
                News.objects.create(
                    title=title,
                    content=str(content),
                    url=a['href'],
                    author='AutoNews.ru',
                    img=img,
                    category=Category.objects.get(name='Авто')
                )
            except:
                print()

        except:
            print()
