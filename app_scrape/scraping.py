import requests
from bs4 import BeautifulSoup


def sea(goods):
    url = 'https://search.rakuten.co.jp/search/mall/{}'.format(goods)

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    items = soup.select('.searchresultitem', limit=10)


    n = 1

    data_rakuten = []

    for index, item in enumerate(items):
        title = item.select_one('.title').text.replace('\n', '')
        price = item.select_one('.price').text.replace(
            '\n', '').replace(' ', '')
        url = item.find('a').get('href')
        price_num = item.find('span', attrs={'class': 'important'}).text.replace('円','').replace(',','')
        price_num = int(price_num)
        num = index + 1


        # print('商品名：{}　価格：{}'.format(title,price))
        # print('-'*30)
        # print(url)
        data_rakuten.append([title, price, url, price_num, num])

        if n > 9:
            break
        n += 1

    return data_rakuten


def sea_min(goods):
    url = 'https://search.rakuten.co.jp/search/mall/{}?s=2'.format(goods)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    items = soup.select('.searchresultitem', limit=10)


    n = 1

    data_rakuten = []

    for index, item in enumerate(items):
        title = item.select_one('.title').text.replace('\n', '')
        price = item.select_one('.price').text.replace(
            '\n', '').replace(' ', '')
        url = item.find('a').get('href')
        
        price_num = item.find('span', attrs={'class': 'important'}).text.replace('円','').replace(',','')
        price_num = int(price_num)
        num = index + 1

        # print('商品名：{}　価格：{}'.format(title,price))
        # print('-'*30)
        # print(url)
        data_rakuten.append([title, price, url, price_num, num])

        if n > 10:
            break
        n += 1

    return data_rakuten