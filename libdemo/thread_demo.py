import threading
from threading import Thread


def print_numbers():
    for i in range(1, 11):
        print('Child ', i)


print(threading.current_thread().name)
ct = Thread(target=print_numbers)
ct.start()

ct.join()  # make current thread wait until ct is terminated

for i in range(1, 11):
    print('Main', i)
