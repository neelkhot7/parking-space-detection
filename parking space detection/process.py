import multiprocessing
import time

BUFFER_SIZE = 5
q = multiprocessing.Queue(BUFFER_SIZE)

def producer(numbers):
    for i in numbers:
        q.put(i)
        print(f"Producer produced-{i}")
        time.sleep(1)

def consumer(num_items):
    for _ in range(num_items):
        if not q.empty():
            item = q.get()
            print(f"Consumer consumed-{item}")
            time.sleep(0.1)
        else:
            print("Consumer: Buffer is empty")
            time.sleep(0.1)

if __name__ == "__main__":
    numbers = [x for x in range(10)]

    producer_process = multiprocessing.Process(target=producer, args=(numbers,))
    consumer_process = multiprocessing.Process(target=consumer, args=(len(numbers),))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()
