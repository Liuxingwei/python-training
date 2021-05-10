from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
    return os.getpid(), x*x

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=8) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(f, range(100)))

        print(pool.imap(f, range(10)))
