"""
LC 472
"""


class Solution:  # pylint: disable=too-few-public-methods

    """
    Solution of LC 472
    """

    @staticmethod
    def find_all_concatenated_words_in_a_dict(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words_set = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                if (word[:i] in words_set) and ((word[i:] in words_set) or dfs(word[i:])):
                    return True
            return False
        return [word for word in words if dfs(word)]
