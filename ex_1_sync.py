import os, sys
from time import time

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

def get_product_info(i, url):
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    
    product = {
        'name': soup.find(itemprop='name').text,
        'price': float(soup.find(itemprop='price').attrs['content'])
    }

    print(f'{i}, {product}')

if __name__ == '__main__':
    start = time()

    urls = get_urls('https://www.dafiti.com.br/calcados-masculinos/botas/')

    for i, url in enumerate(urls):
        get_product_info(i, url)

    write_on_file(os.path.basename(sys.argv[0]), time() - start)
