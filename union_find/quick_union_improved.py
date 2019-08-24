"""
Quick Union improved
"""


from union_find.quick_union import QuickUnionUF


class QuickUnionImprovedUF(QuickUnionUF):
    """
    class of QuickUnionImproved
    """

    def root(self, node: int) -> int:
        """
        :param node: ...
        :return: ...
        """
        if self._id[node] != node:
            self._id[node] = self.root(self._id[node])
        return self._id[node]
