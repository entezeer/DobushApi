from bs4 import BeautifulSoup
from pip._vendor import requests
import html2text

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
    News.objects.filter(category=Category.objects.get(name='Технологии')).filter(poll__isnull=True).all().delete()
    getHitechNews()
    getItWorldNews()


def getHitechNews():
    response = requests.get('https://hi-tech.news', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('div.post-content a.post-title-a[href]')[0:15]:
        try:
            response_ = requests.get(a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1', class_='title').text

            try:
                images = soup.find('div', {"class": "post-media-full"}).findChildren('img')
                for i in images:
                    img = 'https://hi-tech.news' + i.get('src')
            except:
                img = None

            content = soup.select('div.the-excerpt')[0]

            try:
                saveNews(title, str(content), a['href'], 'Hi-Tech.news', img)
            except:
                print()

        except:
            print()


def getItWorldNews():
    response = requests.get('https://www.it-world.ru/it-news/tech', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('div.title a[href]')[0:10]:
        try:
            response_ = requests.get('https://www.it-world.ru' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1', class_='detail').text

            try:
                images = soup.select('div.detail figure img')
                for i in images:
                    img = 'https://www.it-world.ru' + i.get('src')
            except:
                img = None

            content_ = soup.select('div.detail p')
            content_.remove(content_[0])
            content_.remove(content_[0])
            content = ' '.join([str(elem) for elem in content_])
            try:
                saveNews(title, str(content), 'https://www.it-world.ru' + a['href'], 'It-World.ru', img)
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
            category=Category.objects.get(name='Технологии')
        )
