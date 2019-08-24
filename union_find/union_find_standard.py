"""
Standard Union Find implementation which includes size of a connected component
"""


class UF:
    """
    Standard UF class
    """

    def __init__(self, size: int) -> None:
        """
        :param size: number of nodes
        """
        self._p = list(range(size))
        self._sz = [1] * size  # when size is needed

    def find(self, node: int) -> int:
        """
        :param node: index of node
        :return: index of root of node
        """
        if self._p[node] != node:
            self._p[node] = self.find(self._p[node])
        return self._p[node]

    def union(self, node_x: int, node_y: int) -> None:
        """
        :param node_x: index of node to union
        :param node_y: index of node to union
        :return: None
        """
        if self.connected(node_x, node_y):  # when size is needed
            return
        node_x_root = self.find(node_x)
        node_y_root = self.find(node_y)
        self._p[node_x_root] = node_y_root
        self._sz[node_y_root] += self._sz[node_x_root]  # when size is needed

    def connected(self, node_x: int, node_y: int) -> bool:
        """
        :param node_x: index of node to check if connected
        :param node_y: index of node to check if connected
        :return: bool, if node_x and node_y are connected
        """
        return self.find(node_x) == self.find(node_y)

    def size(self, node: int) -> int:
        """
        :param node: index of node to get size of connected component
        :return: int, size of connected component
        """
        return self._sz[self.find(node)]  # when size is needed
