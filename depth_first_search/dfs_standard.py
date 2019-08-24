"""
standard DFS implementation
"""


class DFS:

    """
    standard DFS implementation for graph denoted by adjacency_list
    """

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
        self.visited = set()

    def dfs(self, cur):
        """
        :param cur: current node
        :return: None
        """

        # check/update status of current node
        if cur in self.visited:
            return
        self.visited.add(cur)

        # do something with current node, e.g. check if it is what we are looking for
        # if cur == target:
        #     pass

        # visit next node
        for next_node in self.adjacency_list[cur]:
            self.dfs(next_node)

    def traverse(self, start_node):
        """
        :param start_node: start node
        :return: None
        """
        self.dfs(start_node)
