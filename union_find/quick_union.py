class QuickUnionUF:

    def __init__(self, size: int) -> None:
        self.id = list(range(size))
        self.size = size

    def root(self, i: int) -> int:
        while self.id[i] != i:
            i = self.id[i]
        return i

    def union(self, p: int, q: int) -> None:
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j

    def connected(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)
