from symbol_table.trie import Trie
from unittest import TestCase


class TestTrie(TestCase):

    def test_trie(self):
        trie = Trie()
        self.assertEqual(trie.get('3'), None)
        trie.set('3', 33)
        self.assertEqual(trie.get('33'), None)
        self.assertEqual(trie.get('3'), 33)
        self.assertEqual(trie.get(''), None)
        trie.set('33', 44)
        self.assertEqual(trie.get('33'), 44)
        self.assertEqual(trie.get('333'), None)
