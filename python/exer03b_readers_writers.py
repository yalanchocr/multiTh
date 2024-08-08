'''
THE READERS-WRITERS PROBLEM
Solution for the third readers-writers problem
'''

import random
import time
import threading



class GlobalData:
    def __init__(self):
        self.resource = 0
        self.reader_count = 0
        self.lk_resource = threading.Lock()
        self.lk_reader_count = threading.Lock()
        self.lk_service_queue = threading.Lock()



def do_task_writer(g: GlobalData, delay_time: int):
    time.sleep(delay_time)

    with g.lk_service_queue:
        g.lk_resource.acquire()

    g.resource = random.randint(0, 99)
    print('Write', g.resource)

    g.lk_resource.release()



def do_task_reader(g: GlobalData, delay_time: int):
    time.sleep(delay_time)

    with g.lk_service_queue:
        # Increase reader count
        with g.lk_reader_count:
            g.reader_count += 1

            if g.reader_count == 1:
                g.lk_resource.acquire()

    # Do the reading
    print('Read', g.resource)

    # Decrease reader count
    with g.lk_reader_count:
        g.reader_count -= 1

        if g.reader_count == 0:
            g.lk_resource.release()



gbl_data = GlobalData()
NUM_READERS = 8
NUM_WRITERS = 6

for _ in range(NUM_READERS):
    threading.Thread(target=do_task_reader, args=(gbl_data, random.randint(0, 2))).start()

for _ in range(NUM_WRITERS):
    threading.Thread(target=do_task_writer, args=(gbl_data, random.randint(0, 2))).start()
