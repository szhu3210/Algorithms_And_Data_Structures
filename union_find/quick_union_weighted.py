from union_find.quick_union import QuickUnionUF


class QuickUnionWeightedUF(QuickUnionUF):

    def __init__(self, size: int) -> None:
        super().__init__(size)
        self.sz = [1] * size

    def union(self, p: int, q: int) -> None:
        i = self.root(p)
        j = self.root(q)
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
