import threading
import time

def worker():
    print("Worker thread started")
    time.sleep(2)
    print("Worker thread finished")

if __name__ == "__main__":
    thread = threading.Thread(target=worker)
    thread.start()
    print("Main thread continues")
    thread.join()  # Wait for the thread to finish
    print("Main thread finished")