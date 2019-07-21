from unittest import TestCase
from binary_search.binary_search_standard import find


class TestBinarySearch(TestCase):

    def test_quick_find(self):
        res = find([1, 2, 3, 3, 4, 5], 3)
        self.assertEqual(res, 2)
        res = find([1, 2, 3, 3, 4, 5], 2)
        self.assertEqual(res, 1)
        res = find([1, 2, 3, 3, 4, 5], 1)
        self.assertEqual(res, 0)
        res = find([1, 2, 3, 3, 4, 5], 6)
        self.assertEqual(res, -1)
        res = find([1, 2, 3, 3, 4, 5], 5)
        self.assertEqual(res, 5)
        res = find([1, 2, 4, 5], 3)
        self.assertEqual(res, -1)
        res = find([1, 2], 3)
        self.assertEqual(res, -1)
        res = find([1, 2], 2)
        self.assertEqual(res, 1)
        res = find([1, 2], 1)
        self.assertEqual(res, 0)
        res = find([1], 3)
        self.assertEqual(res, -1)
        res = find([], 3)
        self.assertEqual(res, -1)
