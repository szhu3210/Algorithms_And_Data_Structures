"""
Test for Trie class
"""


from unittest import TestCase
from symbol_table.trie import Trie


class TestTrie(TestCase):
    """
    Test class
    """

    def test_trie(self):
        """
        :return: None
        """
        trie = Trie()
        self.assertEqual(trie.get('3'), None)
        trie.set('3', 33)
        self.assertEqual(trie.get('33'), None)
        self.assertEqual(trie.get('3'), 33)
        self.assertEqual(trie.get(''), None)
        trie.set('3', 44)
        self.assertEqual(trie.get('3'), 44)
        self.assertEqual(trie.get('333'), None)
