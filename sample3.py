import concurrent.futures

def worker(n):

    return n * 2

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(worker, range(10))

    for result in results:
        print(result)
