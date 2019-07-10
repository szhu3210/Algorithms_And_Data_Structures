from depth_first_search.dfs_standard import DFS


class DFSDetectCycles(DFS):

    def dfs_detect_cycles(self, cur):

        if self.visited[cur]:
            return True
        self.visited[cur] = True

        for node in self.g[cur]:
            if self.dfs_detect_cycles(node):
                return True
        
        return False
