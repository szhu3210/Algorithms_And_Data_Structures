from union_find.Practice_1_LC_952_Hard.Practice_1_LC_952_Hard_test import TestLC952
from union_find.Practice_2_LC_803_Hard.Practice_2_LC_803_Hard_test import TestLC803
from union_find.quick_find import QuickFindUF
from union_find.quick_union import QuickUnionUF
from union_find.quick_union_improved import QuickUnionImprovedUF
from union_find.quick_union_weighted import QuickUnionWeightedUF
from union_find.quick_union_weighted_path_compression import QuickUnionWeightedPathCompressionUF
from union_find.union_find_standard import UF


class TestUnionFind(TestLC952, TestLC803):

    @staticmethod
    def unified_test(cls) -> bool:

        with open('input', 'r') as f:
            str_in = list(map(lambda s: list(map(lambda n: int(n), s.split())), f.readlines()))

        with open('output', 'r') as f:
            str_out = list(map(lambda s: list(map(lambda n: int(n), s.split())), f.readlines()))

        # print(str_in)
        # print(str_out)

        res = []
        uf = cls(str_in[0][0])
        for p, q in str_in[1:]:
            if not uf.connected(p, q):
                uf.union(p, q)
                res.append([p, q])
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
        res = self.unified_test(QuickFindUF)
        self.assertTrue(res)

    def test_quick_union(self):
        res = self.unified_test(QuickUnionUF)
        self.assertTrue(res)

    def test_quick_union_improved(self):
        res = self.unified_test(QuickUnionImprovedUF)
        self.assertTrue(res)

    def test_quick_union_weighted(self):
        res = self.unified_test(QuickUnionWeightedUF)
        self.assertTrue(res)

    def test_quick_union_weighted_path_compression(self):
        res = self.unified_test(QuickUnionWeightedPathCompressionUF)
        self.assertTrue(res)

    def test_union_find_standard(self):
        res = self.unified_test(UF)
        self.assertTrue(res)
