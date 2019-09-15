"""
BIT implementation
"""


class BIT:
    """
    BIT data structure is used to calculate prefix sum of an array in O(logN) time,
     and can update value in O(logN) time.
    Space complexity is O(N).
    """

    def __init__(self, p):
        if isinstance(p, int):
            self.size = p
            self.bit = [0] * (self.size + 1)
        elif isinstance(p, list):
            self.size = len(p)
            self.bit = [0] * (self.size + 1)
            for i, val in enumerate(p):
                self.set(i, val)

    def get(self, i):
        """
        Get prefix sum of index i, inclusive.
        :param i: int
        :return: int
        """
        prefix_sum = 0
        i += 1
        while i > 0:
            prefix_sum += self.bit[i]
            i -= i & (-i)
        return prefix_sum

    def set(self, i, val):
        """
        Update value of index i.
        :param i: int
        :param val: int, incremental
        :return: None
        """
        i += 1
        while i <= self.size:
            self.bit[i] += val
            i += i & (-i)


def test():
    """
    Test BIT class.
    :return: None
    """
    freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]

    bit = BIT(freq)
    print(f"Sum of elements in arr[0..5] is {bit.get(5)}.")

    bit.set(3, 6)
    print(f"Sum of elements in arr[0..5] after update is {bit.get(5)}.")


test()
