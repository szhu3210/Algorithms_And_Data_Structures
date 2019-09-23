"""
Yet another way to serialize or deserialize a tree
"""


# Definition for a binary tree node.
class TreeNode:  # pylint: disable=too-few-public-methods
    """
    Modified TreeNode
    """

    def __init__(self, x, left=None, right=None):
        """
        :param x: int
        :param left: TreeNode
        :param right: TreeNode
        """
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'

    __str__ = __repr__


class Codec:
    """
    Codec
    """

    @staticmethod
    def serialize(root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return str(root)

    @staticmethod
    def deserialize(data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return eval(data)  # pylint: disable=eval-used


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


def test():
    """
    Test
    :return: None
    """
    codec = Codec()
    a_root = TreeNode(1, TreeNode(2), None)
    # print(a_root.__hash__())
    a_root.val = 2
    # print(a_root.__hash__())
    a_s = codec.serialize(a_root)
    print(a_s)
    a_d = codec.deserialize(a_s)
    print(a_d)


# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    test()
