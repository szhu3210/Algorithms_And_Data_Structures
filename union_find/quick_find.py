"""
Quick Find UF implementation
"""


class QuickFindUF:
    """
    QuickFind class
    """

    def __init__(self, size: int):
        self._id = list(range(size))
        self.size = size

    def union(self, node_1: int, node_2: int) -> None:
        """
        :param node_1: node index
        :param node_2: node index
        :return: None
        """
        node_1_id = self._id[node_1]
        node_2_id = self._id[node_2]
        for i in range(self.size):
            if self._id[i] == node_1_id:
                self._id[i] = node_2_id

    def connected(self, node_1: int, node_2: int) -> bool:
        """
        :param node_1: node index
        :param node_2: node index
        :return: bool
        """
        return self._id[node_1] == self._id[node_2]
