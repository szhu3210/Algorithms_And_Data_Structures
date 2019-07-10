class QuickFindUF:

    def __init__(self, size: int):
        self.id = list(range(size))
        self.size = size

    def union(self, p: int, q: int) -> None:
        pid = self.id[p]
        qid = self.id[q]
        for i in range(self.size):
            if self.id[i] == pid:
                self.id[i] = qid

    def connected(self, p: int, q: int) -> bool:
        return self.id[p] == self.id[q]
