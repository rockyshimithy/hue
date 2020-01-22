import os, sys, time
from concurrent.futures import ProcessPoolExecutor, as_completed

from utils import is_prime


NUMBERS = [
    2447109360961063, 1637027521802551, 4350190374376723, 1570341764013157,
    9010435374376723, 1880450821379411, 1893530391196711, 7437672343501903
]

def time_elapsed_by_prime(n):
    start = time.perf_counter()
    return (is_prime(n), time.perf_counter() - start)

def main(workers):
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=workers) as execs:
        process = {execs.submit(time_elapsed_by_prime, n): n for n in NUMBERS}

        for future in as_completed(process):
            res, time_elapsed = future.result()
            msg = 'is' if res else 'is not'
            print(f'({time_elapsed:0.5f}s) {process[future]} {msg} prime')

    print(f'Finished with: {time.perf_counter() - start}s')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        workers = int(sys.argv[1])
    else:
        workers = os.cpu_count()

    main(workers)