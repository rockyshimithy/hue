import os, sys
from time import time, sleep
from threading import Event, Thread
from queue import Queue

import requests
from bs4 import BeautifulSoup as bs

from utils import write_on_file

event = Event()
queue = Queue()


class Worker(Thread):
    def __init__(self, target, queue, name='Worker'):
        super().__init__()
        self.name = name
        self.queue = queue
        self._target = target
        self._stoped = False
        # print(self.name, 'started')

    def run(self):
        event.wait()
        i = 0
        while not self.queue.empty():
            product = self.queue.get()
            # print(self.name, product)
            if product == 'Kill':
                self.queue.put(product)
                self._stoped = True
                break
            self._target(i, product)
            i+=1

    def join(self):
        while not self._stoped:
            sleep(0.1)

def get_urls(category_url):
    response = requests.get(category_url)
    soup = bs(response.content, 'html.parser')

    products = soup.find_all('a', 'product-box-link')
    for p in products:
        if p.attrs['href']:
            queue.put(p.attrs['href'])

    event.set()
    queue.put('Kill')

def get_product_info(i, url):
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    
    product = {
        'name': soup.find(itemprop='name').text,
        'price': float(soup.find(itemprop='price').attrs['content'])
    }

    print(f'{i}, {product}')

def get_pool(n_th: int):
    """Retorna um número n de Threads."""
    return [
        Worker(
            target=get_product_info,
            queue=queue,
            name=f'Worker {n}'
        )
        for n in range(n_th)
    ]


if __name__ == '__main__':
    start = time()

    get_urls('https://www.dafiti.com.br/calcados-masculinos/botas/')

    #print(queue.queue)
    thrs = get_pool(8)

    # print('starts')
    [th.start() for th in thrs]

    # print('joins')
    [th.join() for th in thrs]

    write_on_file(os.path.basename(sys.argv[0]), time() - start)

