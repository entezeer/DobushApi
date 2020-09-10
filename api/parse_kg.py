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
    sputnik()
    vesti()
    mk()
    gezitter()

def sputnik():
    response = requests.get('https://ru.sputnik.kg/news', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('h2.b-plainlist__title a[href]')[0:10]:
        try:
            response_ = requests.get('https://ru.sputnik.kg' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('div', class_='b-article__header-title').text
            print(title)

            try:
                images = soup.find('div', {"class": "b-article__header"}).findChildren('img')
                for i in images:
                    img = i.get('src')
            except:
                img = None

            content = soup.select('div.b-article')
            print(content)

            try:
                News.objects.create(
                    title=title,
                    content=str(content),
                    url='https://ru.sputnik.kg/news' + a['href'],
                    author='Sputnik.kg',
                    img=img,
                    category=Category.objects.get(name='В Кыргызстане')
                )
            except: print()
        except:
            print()

def vesti():
    response = requests.get('https://vesti.kg', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('div.itemBody h2 a[href]')[0:10]:
        try:
            response_ = requests.get('https://vesti.kg' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1').text
            print(title)

            content = soup.select('div.itemBody')
            print(content)

            try:
                News.objects.create(
                    title=title,
                    content=str(content),
                    url='https://vesti.kg' + a['href'],
                    author='Vesti.kg',
                    img=None,
                    category=Category.objects.get(name='В Кыргызстане')
                )
            except: print()
        except:
            print()

def gezitter():
    response = requests.get('https://m.gezitter.org', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('ul.newsBlock li a[href]')[0:10]:
        try:
            response_ = requests.get('https://m.gezitter.org' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1', class_='mgb6').text
            print(title)

            try:
                images = soup.find('div', {"id": "mainNew"}).findChildren('img')
                for i in images:
                    img = 'https://m.gezitter.org' + i.get('src')
            except:
                img = None

            print(img)

            content = soup.select('div#mainNew p')
            print(content[0])

            try:
                News.objects.create(
                    title=title,
                    content=str(content),
                    url='https://vesti.kg' + a['href'],
                    author='Vesti.kg',
                    img=img,
                    category=Category.objects.get(name='В Кыргызстане')
                )
            except: print()
        except:
            print()

def mk():
    response = requests.get('https://www.mk.ru/news', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('li.news__item_hot a[href]')[0:10]:
        try:
            response_ = requests.get(a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1', class_='article__title').text
            print(title)

            try:
                img = soup.find('img', {"class": "article__picture-image"}).get('src')
            except:
                img = None

            print(img)

            content = soup.select('div.article__body')
            print(content)

            try:
                News.objects.create(
                    title=title,
                    content=str(content),
                    url=a['href'],
                    author='Mk.kg',
                    img=img,
                    category=Category.objects.get(name='В Кыргызстане')
                )
            except: print()
        except: print()