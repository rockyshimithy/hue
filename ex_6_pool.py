import os, sys
from time import time
from multiprocessing import Pool #

import requests
from bs4 import BeautifulSoup as bs

from utils import write_on_file

def get_urls(category_url):
    response = requests.get(category_url)
    soup = bs(response.content, 'html.parser')

    urls = [ 
        p.attrs['href']
        for p in soup.find_all('a', 'product-box-link')
        if p.attrs['href']
    ]

    return urls


def get_product_info(i):
    response = requests.get(urls.pop())
    soup = bs(response.content, 'html.parser')
    
    product = {
        'name': soup.find(itemprop='name').text,
        'price': float(soup.find(itemprop='price').attrs['content'])
    }

    print(f'{i}, {product}')

if __name__ == '__main__':
    start = time()

    urls = get_urls('https://www.dafiti.com.br/calcados-masculinos/botas/')

    workers = Pool(5) #

    tasks = [(i, url) for i, url in enumerate(urls)]

    # sync
    result = workers.map(get_product_info, tasks) #
    #print(result)

    # async
    #result = workers.map_async(get_product_info, tasks) #
    #print('------------COMEÇA')
    #result.wait() #
    #print('------------TERMINA')
    #print(result.get()) #

    write_on_file(os.path.basename(sys.argv[0]), time() - start)

