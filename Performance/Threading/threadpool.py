#!/usr/bin/env python3
import concurrent.futures
import time
# import threading


start = time.perf_counter()
threads = []


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

    # results = [executor.submit(do_something, sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())


# for thread in threads:
#     thread.join()


finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds')
