# from threading import Thread
# import time

def square_numbers(n):
    for i in range(n):
        print(f"{i * i}")
        time.sleep(0.1)


# if __name__ == "__main__":
#     threads = []
#     num_threads = 10

#     for i in range(num_threads):
#         t = Thread(target=square_numbers, args=(10,))
#         threads.append(t)

#     for thread in threads:
#         thread.start()
    
#     for thread in threads:
#         thread.join()


# print("Thread finished.")


from threading import Thread
from queue import Queue
import time

if __name__ == "__main__":
    q = Queue()

    num_threads = 10

    for i in range(num_threads):
        t = Thread(target=square_numbers, args=(10,))
        t.daemon = True
        t.start()
        q.put(t)

    for i in range(num_threads):
        thread = q.get()
        thread.start()


