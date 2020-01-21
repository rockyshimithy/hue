import math
import aiofiles

FILENAME = 'metrics.txt'

def write_on_file(file, metric):
    f = open(FILENAME, 'a')
    f.write(f'{file} took {metric}s \n')
    f.close()

async def awrite_on_file(file, metric):
    async with aiofiles.open(FILENAME, 'a') as f:
        await f.write(f'{file} took {metric}s \n')
        await f.flush()

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    # for x in range(n - 1, 1, -1):
    #     if n % x == 0:
    #         return False

    # return True

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n +1, 2):
        if n % i == 0:
            return False

    return True