from links import URL, params_link, prices_link, title_link
from lxml import html
import requests
import csv

url_link = (URL)

def get_info():
    reque = requests.get(url_link)
    tree = html.fromstring(reque.content)

    '''Парсер заголовка/названия машин'''
    titles = tree.xpath(title_link)

    '''Парсер цен на машин'''
    prices = [
        price.replace(u'\xa0', ' ') for price in tree.xpath(prices_link)
    ]

    '''Парсер параметров машин'''
    params = [
        param.replace(u'\u2009', ' ').replace(u'\xa0', ' ') for param in tree.xpath(params_link)
    ]

    '''Запись в файл auto.csv'''
    with open('auto.csv', mode ='w', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['Название модели', 'Характеристика', 'Стоимость'])
        try:
            for index in range(len(titles)):
                writer.writerow([titles[index], params[index], prices[index]])
        except IndexError:
            print('Парсинг выполнен')
if __name__ == '__main__':
    get_info()