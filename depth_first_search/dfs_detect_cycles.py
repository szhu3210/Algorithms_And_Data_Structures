"""
implementation of detecting if there exists a cycle in a graph
"""


from depth_first_search.dfs_standard import DFS


class DFSDetectCycles(DFS):

    """
    detect if there is any cycle in a graph
    """

    def dfs_detect_cycles(self, cur):

        """
        :param cur:
        :return:
        """

        if self.visited[cur]:
            return True
        self.visited[cur] = True

        for node in self.adjacency_list[cur]:
            if self.dfs_detect_cycles(node):
                return True
        return False
