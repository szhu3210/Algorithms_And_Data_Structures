"""
QuickUnionWeightedUF
"""


from union_find.quick_union import QuickUnionUF


class QuickUnionWeightedUF(QuickUnionUF):
    """
    Weighted QuickUnion
    """

    def __init__(self, size: int) -> None:
        super().__init__(size)
        self._size = [1] * size

    def union(self, node_1: int, node_2: int) -> None:
        """
        :param node_1: ...
        :param node_2: ...
        :return: ...
        """
        node_1_root = self.root(node_1)
        node_2_root = self.root(node_2)
        if self._size[node_1_root] < self._size[node_2_root]:
            self._id[node_1_root] = node_2_root
            self._size[node_2_root] += self._size[node_1_root]
        else:
            self._id[node_2_root] = node_1_root
            self._size[node_1_root] += self._size[node_2_root]
