from multiprocessing import Process
import os
import time


def square_numbers(n):
    for i in range(n):
        print(f"{i * i}")
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

for i in range(num_processes):
    p = Process(target=square_numbers, args=(10,))
    processes.append(p)


for p in processes:
    p.start()

for p in processes:
    p.join()

print("All processes finished.")