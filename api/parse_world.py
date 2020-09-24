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
    News.objects.filter(category=Category.objects.get(name='В мире')).all().delete()
    mir24()
    bbc()


def lenta():
    responce = session.get('https://lenta.ru/rss/news', headers=headers)

    bs = BeautifulSoup(responce.text, 'lxml')
    item = [i for i in bs.find_all('item')][0:10]
    for j in item:
        try:
            # print(j)
            soup = BeautifulSoup(j.text, 'lxml')
            # print(soup)

            title = j.title
            # print(title)
            content = soup.find('description')
            img = soup.enclosure.url
            url = soup.link

            News.objects.create(
                    title=title,
                    content=str(content),
                    url=url,
                    author='Lenta.ru',
                    img=img,
                    category=Category.objects.get(name='В мире')
            )
        except:
            print()


def mir24():
    response = session.get('https://mir24.tv/news/list/all', headers=headers)

    bs = BeautifulSoup(response.text, 'lxml')
    source = [a['href'] for a in bs.find_all('a', {'class': 'nc-link'})][0:10]
    for j in source:
        try:
            response_ = session.get(j, headers=headers)
            soup = BeautifulSoup(response_.text, 'lxml')

            title = soup.find('h1', class_='post-title').get_text()

            content = soup.find('div', class_='article-content js-mediator-article')

            News.objects.create(
                    title=title,
                    content=str(content),
                    url=j,
                    author='Mir24.tv',
                    img=None,
                    category=Category.objects.get(name='В мире')
            )
        except:
            print()


def bbc():
    response = session.get('https://www.bbc.com/russian', headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    source = [a['href'] for a in bs.find_all('a', {'class': 'Link-sc-1dvfmi3-5 jeUMCT'})][0:10]
    for j in source:
        try:
            response_ = session.get('https://www.bbc.com' + j, headers=headers)
            soup = BeautifulSoup(response_.text, 'lxml')
            try:
                img = soup.find('img', class_='js-image-replace').get('src')
            except:
                img = None

            title = soup.find(class_='story-body__h1').get_text()

            content = soup.find(class_='story-body__inner')
            News.objects.create(
                    title=title,
                    content=str(content),
                    url='https://www.bbc.com' + j,
                    author='BBC Russian',
                    img=img,
                    category=Category.objects.get(name='В мире')
            )
        except:
            print()


def regnum():
    print()


def deutcheWelle():
    print()
