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
    News.objects.filter(category=Category.objects.get(name='В Кыргызстане')).filter(poll__isnull=True).all().delete()
    getSputnikNews()
    getVestiKgNews()
    # mk()
    getAkipressNews()


def getSputnikNews():
    response = requests.get('https://ru.sputnik.kg/news', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('h2.b-plainlist__title a[href]')[0:10]:
        try:
            response_ = requests.get('https://ru.sputnik.kg' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('div', class_='b-article__header-title').text

            try:
                images = soup.find('div', {"class": "b-article__header"}).findChildren('img')
                for i in images:
                    img = i.get('src')
            except:
                img = None

            content = soup.select('div.b-article__text')[0]

            try:
                saveNews(title, str(content), 'https://ru.sputnik.kg' + a['href'], 'Sputnik.kg', img)
            except:
                print()
        except:
            print()


def getVestiKgNews():
    response = requests.get('https://vesti.kg', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('div.itemBody h2 a[href]')[0:10]:
        try:
            response_ = requests.get('https://vesti.kg' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1').text

            content = soup.select('div.itemBody')[0]

            try:
                saveNews(title, str(content), 'https://vesti.kg' + a['href'], 'Vesti.kg', None)
            except:
                print()
        except:
            print()


def getAkipressNews():
    response = requests.get('https://kg.akipress.org/?news&place=show_v2', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('div.news_list div.elem a')[0:10]:
        try:
            response_ = requests.get(a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1', class_='news-title').text

            try:
                images = soup.find('div', {"class": "cast_elem_content"}).findChildren('img')
                for i in images:
                    img = 'https:' + i.get('src')
            except:
                img = None

            content = soup.select('div.colored-link-text')

            try:
                saveNews(title, str(content[0]), a['href'], 'Akipress.org', img)
            except:
                print()
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

            try:
                img = soup.find('img', {"class": "article__picture-image"}).get('src')
            except:
                img = None


            content = soup.select('div.article__body')

            try:
                saveNews(title, str(content), a['href'], 'Mk.kg', img)
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
            category=Category.objects.get(name='В Кыргызстане')
        )
