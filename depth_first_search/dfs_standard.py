class DFS:
    def __init__(self, size, adjacency_list):
        self.n = size
        self.g = adjacency_list
        self.visited = [False] * size

    def dfs(self, cur):

        # check/update status of current node
        if self.visited[cur]:
            return
        self.visited[cur] = True

        # visit next node
        for next_node in self.g[cur]:
            self.dfs(next_node)

    def traverse(self, start_node=0):
        self.dfs(start_node)
