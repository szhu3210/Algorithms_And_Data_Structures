"""
Trie tree is one of symbol table implementations
Suitable for string key
Sub-linear performance
"""

from collections import defaultdict


class Trie:

    class Node:
        def __init__(self):
            self.value = None
            self.next = defaultdict(Trie.Node)

    def __init__(self):
        self.root = Trie.Node()

    def set(self, key, value):
        cur = self.root
        for c in key:
            cur = cur.next[c]
        cur.value = value

    def get(self, key):
        cur = self.root
        for c in key:
            if c not in cur.next:
                return None
            cur = cur.next[c]
        return cur.value
