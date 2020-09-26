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
    News.objects.filter(category=Category.objects.get(name='Кино')).all().delete()
    getMovieNews()


def getMovieNews():
    response = requests.get('https://www.kinopoisk.ru/media/news', headers=headers)
    bs = BeautifulSoup(response.content, 'lxml')
    for a in bs.select('div.posts-grid__main-section-column a.WH0s4mM3McoTk8gEm5kNm[href]')[0:20]:
        try:
            response_ = requests.get('https://www.kinopoisk.ru' + a['href'], headers=headers)
            soup = BeautifulSoup(response_.content, 'lxml')
            title = soup.find('h1',
                              class_='media-post-title media-post-title_theme_desktop media-post-title_style_news media-news__title').text
            try:
                images = soup.find('div', {"class": "media-news__main-img-container"}).findChildren('img')
                for i in images:
                    img = 'https:' + i.get('src')
            except:
                img = None

            content = soup.select('div.media-post-setka-inner-html')[0]

            try:
                News.objects.create(
                    title=title,
                    content=str(content),
                    url='https://www.kinopoisk.ru' + a['href'],
                    author='Kinopoisk.ru',
                    img=img,
                    category=Category.objects.get(name='Кино')
                )
            except:
                print()

        except:
            print()
