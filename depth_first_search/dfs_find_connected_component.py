"""
find connected component
"""


from depth_first_search.dfs_standard import DFS


class DFSFindConnectedComponent(DFS):

    """
    something
    """

    def __init__(self, adjacency_list):
        super().__init__(adjacency_list)
        self.component = {}
        self.component_id = 0

    def find_components(self):
        """
        :return:
        """
        for node in self.adjacency_list:
            if node not in self.visited:
                self.dfs(node)  # mark component_id when visit nodes
                self.component_id += 1
        return self.component

    def dfs(self, cur):  # this time, cur is guaranteed to be unvisited
        """
        :param cur: ...
        :return: ...
        """
        self.visited.add(cur)
        self.component[cur] = self.component_id
        for node in self.adjacency_list[cur]:
            if node not in self.visited:  # check node (to be unvisited) before calling dfs
                self.dfs(node)
