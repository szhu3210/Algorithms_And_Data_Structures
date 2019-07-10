class UF:

    def __init__(self, size: int) -> None:
        self.p = list(range(size))
        self.sz = [1] * size  # when size is needed

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int) -> None:
        if self.connected(x, y):  # when size is needed
            return
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
        self.sz[yr] += self.sz[xr]  # when size is needed

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x: int) -> int:
        return self.sz[self.find(x)]  # when size is needed
