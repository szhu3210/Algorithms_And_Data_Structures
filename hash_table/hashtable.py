"""
A simple hash table implementation using Python List.
"""


import threading


class HashTable:
    """
    Hash Table class
    """

    def __init__(self, size: int = 100) -> None:
        """
        :param size: size of list initialization
        """
        self.table = [[] for _ in range(size)]
        self.size = size
        self.locks = [threading.Lock() for _ in range(size)]

    def hash(self, val: int) -> int:
        """
        :param val: int
        :return: None
        """
        return val % self.size

    def get(self, key: int) -> int:
        """
        :param key: int
        :return: int
        """
        # self.lock.acquire()
        hashed_key = self.hash(key)
        try:
            for _k, _v in self.table[hashed_key]:
                if _k == key:
                    return _v
        finally:
            # self.lock.release()
            pass
        raise ValueError(f'Key {key} does not exist in hash table.')

    def set(self, key: int, value: int) -> None:
        """
        :param key: int
        :param value: int
        :return: None
        """
        # self.lock.acquire()
        hashed_key = self.hash(key)
        try:
            for i, entry in enumerate(self.table[hashed_key]):
                k, _ = entry
                if k == key:
                    self.table[hashed_key][i] = (k, value)
            self.table[hashed_key].append((key, value))
        finally:
            # self.lock.release()
            pass

    def increment(self, key: int):
        """
        ...
        :param key: ...
        :return: ...
        """
        _h = self.hash(key)
        self.locks[_h].acquire()
        try:
            self.set(key, self.get(key) + 1)
        finally:
            self.locks[_h].release()


def test_sequential(hash_table):
    """
    Test
    :return: None
    """

    for _ in range(5 * 10 ** 2):
        hash_table.increment(101)
        hash_table.increment(102)


def test_multithreading():
    """
    Test under multithreading condition
    :return: None
    """

    hash_table = HashTable(100)
    hash_table.set(101, 0)
    hash_table.set(102, 0)

    print('thread %s is running...' % threading.current_thread().name)
    thread1 = threading.Thread(target=test_sequential, args=(hash_table, ), name='LoopThread 1')
    thread2 = threading.Thread(target=test_sequential, args=(hash_table, ), name='LoopThread 2')
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    assert hash_table.get(101) == 1000
    assert hash_table.get(102) == 1000
    print('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    test_multithreading()
