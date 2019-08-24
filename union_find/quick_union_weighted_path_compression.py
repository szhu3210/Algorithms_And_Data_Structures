"""
Optimized UF
"""


from union_find.quick_union_weighted import QuickUnionWeightedUF


class QuickUnionWeightedPathCompressionUF(QuickUnionWeightedUF):
    """
    Add path compression
    """

    def root(self, node: int) -> int:
        while self._id[node] != node:
            self._id[node] = self._id[self._id[node]]
            node = self._id[node]
        return node
