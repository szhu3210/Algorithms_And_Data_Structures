"""
Trie tree is one of symbol table implementations
Suitable for string key
Sub-linear performance
"""


from collections import defaultdict


class Trie:
    """
    Trie class
    """

    class Node:  # pylint: disable=too-few-public-methods
        """
        Node class
        """
        def __init__(self):
            self.value = None
            self.next = defaultdict(Trie.Node)

    def __init__(self):
        self.root = Trie.Node()

    def set(self, key, value):
        """
        :param key: ...
        :param value: ...
        :return: ...
        """
        cur = self.root
        for character in key:
            cur = cur.next[character]
        cur.value = value

    def get(self, key):
        """
        :param key: ...
        :param value: ...
        :return: ...
        """
        cur = self.root
        for character in key:
            if character not in cur.next:
                return None
            cur = cur.next[character]
        return cur.value
