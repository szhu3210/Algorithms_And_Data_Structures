from union_find.quick_union_weighted import QuickUnionWeightedUF


class QuickUnionWeightedPathCompressionUF(QuickUnionWeightedUF):

    def root(self, i: int) -> int:
        while self.id[i] != i:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i
