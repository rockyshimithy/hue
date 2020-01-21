import os, sys
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
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
    return f'{i}, {product}'

if __name__ == '__main__':
    start = time()

    urls = get_urls('https://www.dafiti.com.br/calcados-masculinos/botas/')

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(get_product_info, i, url)
            for i, url in enumerate(urls)
        ]
    # completed, _ = wait(futures) #

    # for future in completed:
    #     print(future.result())
    for future in as_completed(futures): #
        print(future.result())

    write_on_file(os.path.basename(sys.argv[0]), time() - start)
