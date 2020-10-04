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

# def getNews():
#     News.objects.filter(category=Category.objects.get(name='Иностранные')).all().delete()

def getArabNews():
    response = requests.get('https://www.alarabiya.net/latest-news', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    ar = bs.select('ul#Scroll li a[href]')[0:10]
    newAr = [v for k, v in enumerate(ar) if not k % 2]
    for a in newAr:
        try:
            print(a['href'])
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
                    language=""
                )
            except:
                print()

        except:
            print()
