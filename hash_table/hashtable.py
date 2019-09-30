"""
A simple hash table implementation using Python List.
"""


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

    def hash(self, val: int) -> int:
        """
        :param val: int
        :return: None
        """
        return val % self.size

    def get(self, key: int) -> object:
        """
        :param key: int
        :return: object
        """
        hashed_key = self.hash(key)
        for _k, _v in self.table[hashed_key]:
            if _k == key:
                return _v
        raise ValueError(f'Key {key} does not exist in hash table.')

    def set(self, key: int, value: object) -> None:
        """
        :param key: int
        :param value: object
        :return: None
        """
        hashed_key = self.hash(key)
        for i, entry in enumerate(self.table[hashed_key]):
            k, _ = entry
            if k == key:
                self.table[hashed_key][i] = (k, value)
        self.table[hashed_key].append((key, value))


def test():
    """
    Test
    :return: None
    """
    hash_table = HashTable(100)

    hash_table.set(1, 'one')
    assert hash_table.get(1) == 'one'
    hash_table.set(101, 'one zero one')
    assert hash_table.get(101) == 'one zero one'
    assert hash_table.get(1) == 'one'

    hash_table.set(122, 'one two two')
    assert hash_table.get(122) == 'one two two'

    try:
        print(hash_table.get(123))
    except ValueError:
        pass


if __name__ == '__main__':
    test()
