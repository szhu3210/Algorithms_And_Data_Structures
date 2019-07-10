from union_find.quick_union import QuickUnionUF


class QuickUnionImprovedUF(QuickUnionUF):

    def root(self, i: int) -> int:
        if self.id[i] != i:
            self.id[i] = self.root(self.id[i])
        return self.id[i]
