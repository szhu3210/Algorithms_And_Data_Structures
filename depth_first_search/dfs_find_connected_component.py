from depth_first_search.dfs_standard import DFS


class DFSFindConnectedComponent(DFS):

    def __init__(self, size, adjacency_list):
        super().__init__(size, adjacency_list)

        self.component = [None] * size
        self.component_id = 0

    def find_components(self):
        for node in range(self.n):
            if not self.visited[node]:
                self.dfs(node)  # mark component_id when visit nodes
                self.component_id += 1
        return self.component

    def dfs(self, cur):  # this time, cur is guaranteed to be unvisited

        self.visited[cur] = True

        self.component[cur] = self.component_id

        for node in self.g[cur]:
            if not self.visited[node]:  # check node (to be unvisited) before calling dfs
                self.dfs(node)
