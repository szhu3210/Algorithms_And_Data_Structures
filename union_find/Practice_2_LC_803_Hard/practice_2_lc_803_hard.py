"""
LC 803
"""


from typing import List
from union_find.union_find_standard import UF


def hit_bricks(grid: List[List[int]], hits: List[List[int]]) -> List[int]:  # pylint: disable=too-many-locals, too-many-branches
    """
    :param grid: ...
    :param hits: ...
    :return: ...
    """

    res = []
    len_i, len_j = len(grid), len(grid[0])

    # check invalid hits and move to the final state
    for ind, hit in enumerate(hits):
        i, j = hit
        if grid[i][j] == 0:
            hits[ind] = []
        grid[i][j] = 0

    # define UF and ceiling
    _uf = UF(len_i * len_j + 1)
    ceiling_index = len_i * len_j

    # mapping from brick to its id in UF
    def bid(grid_i, grid_j):
        return grid_i * len_j + grid_j

    # initialize UF
    for j in range(len_j):
        if grid[0][j] == 1:
            _uf.union(ceiling_index, bid(0, j))

    for i in range(len_i):
        for j in range(len_j):
            if grid[i][j] == 0:
                continue
            for n_i, n_j in [(i - 1, j), (i, j - 1)]:
                if 0 <= n_i < len_i and 0 <= n_j < len_j and grid[n_i][n_j] == 1:
                    _uf.union(bid(i, j), bid(n_i, n_j))

    # add brick to the grid, calculating change of bricks
    for hit in hits[::-1]:

        if not hit:
            res.append(0)
            continue

        before_add = _uf.size(ceiling_index)

        i, j = hit
        grid[i][j] = 1
        if i == 0:
            _uf.union(ceiling_index, bid(i, j))
        for n_i, n_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= n_i < len_i and 0 <= n_j < len_j and grid[n_i][n_j] == 1:
                _uf.union(bid(i, j), bid(n_i, n_j))

        after_add = _uf.size(ceiling_index)

        drop = after_add - before_add
        res.append(max(0, drop - 1))

    return res[::-1]
