import asyncio, os, sys
from time import time

import aiohttp
import uvloop
from bs4 import BeautifulSoup as bs

from utils import awrite_on_file

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()


async def get_urls(category_url):
    async with aiohttp.ClientSession(loop=loop) as client:
        async with client.get(category_url) as response:
            content = await response.read()
    
    soup = bs(content, 'html.parser')

    urls = [ 
        p.attrs['href']
        for p in soup.find_all('a', 'product-box-link')
        if p.attrs['href']
    ]

    return urls

async def get_product_info(i, url):
    async with aiohttp.ClientSession(loop=loop) as client:
        async with client.get(url) as response:
            content = await response.read()
    
    soup = bs(content, 'html.parser')
    
    product = {
        'name': soup.find(itemprop='name').text,
        'price': float(soup.find(itemprop='price').attrs['content'])
    }

    print(f'{i}, {product}')

if __name__ == '__main__':
    
    start = time()

    urls = loop.run_until_complete(
        get_urls('https://www.dafiti.com.br/calcados-masculinos/botas/')
    )

    tasks = [ get_product_info(i, url) for i, url in enumerate(urls) ]

    loop.run_until_complete(asyncio.gather(*tasks))
    
    loop.run_until_complete(
        awrite_on_file(os.path.basename(sys.argv[0]), time() - start)
    )
    
    loop.close()
