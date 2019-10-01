"""
Segment Tree standard implementation
"""


from typing import List, Optional


class NumArray:
    """
    Range query mutable - LeetCode 307
    """

    class STNode:  # pylint: disable=too-few-public-methods
        """
        Segment Tree Node structure
        """

        def __init__(self, l, r, v, left=None, right=None):  # pylint: disable=too-many-arguments
            self.left_bound = l
            self.right_bound = r
            self.value = v
            self.left_child = left
            self.right_child = right

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = self.build(0, len(nums) - 1)

    def build(self, i: int, j: int) -> Optional[STNode]:  # pylint: disable=undefined-variable
        """
        Initialize a tree from nums
        :param i: left bound index
        :param j: right bound index
        :return: STNode
        """
        if i > j:
            return None
        if i == j:
            return self.STNode(i, j, self.nums[i])
        mid = (i + j) // 2
        left = self.build(i, mid)
        right = self.build(mid + 1, j)
        return self.STNode(i, j, left.value + right.value, left, right)

    def update(self, index: int, val: int) -> None:
        """
        Update index i with val
        :param index: index in nums
        :param val: value to update
        :return: None
        """

        def dfs(cur_node, index, value):
            """
            ...
            :param cur_node: ...
            :param index: ...
            :param value: ...
            :return: ...
            """
            if not cur_node:
                return
            if cur_node.left_bound == cur_node.right_bound == index:
                cur_node.value = value
                return
            mid = (cur_node.left_bound + cur_node.right_bound) // 2
            if index <= mid:
                dfs(cur_node.left_child, index, value)
            else:
                dfs(cur_node.right_child, index, value)
            cur_node.value = cur_node.left_child.value + cur_node.right_child.value

        dfs(self.root, index, val)

    def range_query(self, _i: int, _j: int) -> int:
        """
        Query based on range of i and j inclusive
        :param _i: ...
        :param _j: ...
        :return: ...
        """

        def dfs(cur_node: Optional[NumArray.STNode], _l, _r):
            if not cur_node:
                return None
            if cur_node.left_bound == _l and cur_node.right_bound == _r:
                return cur_node.value
            mid = (cur_node.left_bound + cur_node.right_bound) // 2
            if _r <= mid:
                return dfs(cur_node.left_child, _l, _r)
            if _l > mid:
                return dfs(cur_node.right_child, _l, _r)
            return dfs(cur_node.left_child, _l, mid) + dfs(cur_node.right_child, mid + 1, _r)

        return dfs(self.root, _i, _j)


def test():
    """
    Test the NumArray class.
    :return: None
    """
    _na = NumArray([1, 2, 3, 6, 5, 7, 8, 34, 5, 62, 11, 634, 3])
    assert _na.range_query(0, 0) == 1
    assert _na.range_query(0, 1) == 3
    assert _na.range_query(0, 2) == 6
    assert _na.range_query(0, 3) == 12
    assert _na.range_query(1, 3) == 11
    assert _na.range_query(1, 5) == 23
    assert _na.range_query(1, 12) == 780
    assert _na.range_query(0, 12) == 781
    _na.update(0, 101)
    assert _na.range_query(0, 12) == 881
    _na.update(0, 301)
    assert _na.range_query(0, 3) == 312
    _na.update(12, 103)
    assert _na.range_query(0, 12) == 1181


if __name__ == '__main__':
    test()
