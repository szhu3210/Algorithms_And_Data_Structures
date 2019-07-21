"""
standard DFS implementation
"""


class DFS:

    """
    standard DFS implementation for graph denoted by adjacency_list
    """

    def __init__(self, size, adjacency_list):
        self.size = size
        self.adjacency_list = adjacency_list
        self.visited = [False] * size

    def dfs(self, cur):
        """
        :param cur:
        :return:
        """

        # check/update status of current node
        if self.visited[cur]:
            return
        self.visited[cur] = True

        # visit next node
        for next_node in self.adjacency_list[cur]:
            self.dfs(next_node)

    def traverse(self, start_node=0):
        """
        :param start_node:
        :return:
        """
        self.dfs(start_node)
