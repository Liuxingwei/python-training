import threading
import time

lock = threading.Lock()
class myThread (threading.Thread):
    def __init__(self, threadID, name, other = None):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.other = other
    def run(self):
        print ("开始线程：" + self.name)
        l = lock.acquire(False)
        print(l)
        if l:
            if self.other is not None:
                self.other.start()
                self.other.join()
            lock.release()
        print ("退出线程：" + self.name)

def print_time(thread, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (thread.name, time.ctime(time.time())))
        counter -= 1

thread1 = myThread(1, "Thread-1")
thread2 = myThread(2, "Thread-2", thread1)
thread2.start()
thread2.join()

import threading
se = threading.BoundedSemaphore(2)
se.acquire()
se.acquire()
se.release()
se.release()
se.release()
se.release()
se.acquire()
se.acquire()
se.acquire()
se.acquire()
