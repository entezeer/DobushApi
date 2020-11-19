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
    News.objects.filter(category=Category.objects.get(name='В мире')).filter(poll__isnull=True).all().delete()
    mir24()
    bbc()
    lenta()


def lenta():
    response = session.get('https://lenta.ru/rss/news', headers=headers)
    bs = BeautifulSoup(response.text, 'html.parser')
    for a in bs.select('item')[0:10]:
        try:
            try:
                img = a.find('enclosure').get('url')
            except:
                img = None

            title = a.find('title').text

            content = a.find('description').text

            url = a.find('guid').text

            saveNews(title, content, url, 'Lenta.ru', img)
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

            saveNews(title, str(content), j, 'Mir24.tv', None)
        except:
            print()


def bbc():
    response = session.get('https://www.bbc.com/russian', headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    for a in bs.select('li div a[href]')[0:15]:
        try:
            response_ = session.get('https://www.bbc.com' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.text, 'lxml')
            try:
                imgs = soup.select('figure div img')
                for i in imgs:
                    img = i.get('src')
            except:
                img = None

            title = soup.find('h1', id='content').get_text()

            content_ = soup.select('main div p')

            content = ' '.join([str(elem) for elem in content_])

            saveNews(title, str(content), 'https://www.bbc.com' + a['href'], 'BBC Russian', img)
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
            category=Category.objects.get(name='В мире')
        )
