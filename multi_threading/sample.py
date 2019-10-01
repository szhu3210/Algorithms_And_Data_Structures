"""
Sample of multithreading in Python.
"""


import time
import threading


def loop():
    """
    Show a thread.
    :return: ...
    """
    print('thread %s is running...' % threading.current_thread().name)
    _ = 0
    while _ < 5:
        _ = _ + 1
        print('thread %s >>> %s' % (threading.current_thread().name, _))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def test():
    """
    ...
    :return: ...
    """
    print('thread %s is running...' % threading.current_thread().name)
    thread1 = threading.Thread(target=loop, name='LoopThread 1')
    thread2 = threading.Thread(target=loop, name='LoopThread 2')
    thread1.start()
    thread2.start()
    # t1.join()
    # t2.join()
    print('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    test()
