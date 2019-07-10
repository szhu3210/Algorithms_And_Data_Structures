from typing import List
from union_find.union_find_standard import UF


class Interview:

    @staticmethod
    def hit_bricks(grid: List[List[int]], hits: List[List[int]]) -> List[int]:

        res = []
        m, n = len(grid), len(grid[0])

        # check invalid hits and move to the final state
        for ind, hit in enumerate(hits):
            i, j = hit
            if grid[i][j] == 0:
                hits[ind] = None
            grid[i][j] = 0

        # define UF and ceiling
        uf = UF(m * n + 1)
        c = m * n

        # mapping from brick to its id in UF
        def bid(gi, gj):
            return gi * n + gj

        # initialize UF
        for j in range(n):
            if grid[0][j] == 1:
                uf.union(c, bid(0, j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for ii, jj in [(i - 1, j), (i, j - 1)]:
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                        uf.union(bid(i, j), bid(ii, jj))

        # add brick to the grid, calculating change of bricks
        for hit in hits[::-1]:

            if hit is None:
                res.append(0)
                continue

            before_add = uf.size(c)

            i, j = hit
            grid[i][j] = 1
            if i == 0:
                uf.union(c, bid(i, j))
            for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                    uf.union(bid(i, j), bid(ii, jj))

            after_add = uf.size(c)

            drop = after_add - before_add
            res.append(max(0, drop - 1))

        return res[::-1]
