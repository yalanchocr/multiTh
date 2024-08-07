import threading

local_data = threading.local()


def worker():
    local_data.my_data = 'hello'
    print(local_data.my_data)


threads = []
for _ in range(4):
    thread = threading.Thread(target=worker)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
