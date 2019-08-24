"""
QuickUnion implementation of UF
"""


class QuickUnionUF:
    """
    Quick Union
    """

    def __init__(self, size: int) -> None:
        self._id = list(range(size))
        self.size = size

    def root(self, node: int) -> int:
        """
        :param node: ...
        :return: ...
        """
        while self._id[node] != node:
            node = self._id[node]
        return node

    def union(self, node_1: int, node_2: int) -> None:
        """
        :param node_1: ...
        :param node_2: ...
        :return: ...
        """
        node_1_id = self.root(node_1)
        node_2_id = self.root(node_2)
        self._id[node_1_id] = node_2_id

    def connected(self, node_1: int, node_2: int) -> bool:
        """
        :param node_1: ...
        :param node_2: ...
        :return: ...
        """
        return self.root(node_1) == self.root(node_2)
