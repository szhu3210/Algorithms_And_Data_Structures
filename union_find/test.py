"""
Test for UF API
"""


from union_find.Practice_1_LC_952_Hard.practice_1_lc_952_hard_test import TestLC952
from union_find.Practice_2_LC_803_Hard.practice_2_lc_803_hard_test import TestLC803
from union_find.quick_find import QuickFindUF
from union_find.quick_union import QuickUnionUF
from union_find.quick_union_improved import QuickUnionImprovedUF
from union_find.quick_union_weighted import QuickUnionWeightedUF
from union_find.quick_union_weighted_path_compression import QuickUnionWeightedPathCompressionUF
from union_find.union_find_standard import UF


class TestUnionFind(TestLC952, TestLC803):
    """
    Test class
    """

    @staticmethod
    def unified_test(_class) -> bool:
        """
        :param _class: ...
        :return: ...
        """

        with open('input', 'r') as file:
            str_in = list(map(lambda s: list(map(int, s.split())), file.readlines()))

        with open('output', 'r') as file:
            str_out = list(map(lambda s: list(map(int, s.split())), file.readlines()))

        # print(str_in)
        # print(str_out)

        res = []
        _uf = _class(str_in[0][0])
        for node_1, node_2 in str_in[1:]:
            if not _uf.connected(node_1, node_2):
                _uf.union(node_1, node_2)
                res.append([node_1, node_2])
                # print(uf.id)
        # if str_out != res:
        #     print(str_out)
        #     print(res)
        #     print('fail')
        # else:
        #     print('pass')
        # self.assertEqual(str_out, res)
        return str_out == res

    def test_quick_find(self):
        """
        :return: ...
        """
        res = self.unified_test(QuickFindUF)
        self.assertTrue(res)

    def test_quick_union(self):
        """
        :return: ...
        """
        res = self.unified_test(QuickUnionUF)
        self.assertTrue(res)

    def test_quick_union_improved(self):
        """
        :return: ...
        """
        res = self.unified_test(QuickUnionImprovedUF)
        self.assertTrue(res)

    def test_quick_union_weighted(self):
        """
        :return: ...
        """
        res = self.unified_test(QuickUnionWeightedUF)
        self.assertTrue(res)

    def test_quick_union_weighted_path_compression(self):
        """
        :return: ...
        """
        res = self.unified_test(QuickUnionWeightedPathCompressionUF)
        self.assertTrue(res)

    def test_union_find_standard(self):
        """
        :return: ...
        """
        res = self.unified_test(UF)
        self.assertTrue(res)
