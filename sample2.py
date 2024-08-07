import threading
import time

counter = 0
def increment_not_safe():
    global counter
    for _ in range(10):
        counter += 1
        time.sleep(1)

def increment():
    global counter
    for _ in range(1000000):
        with lock:
            counter += 1

if __name__ == "__main__":
    lock = threading.Lock()
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=increment_not_safe)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(counter)
