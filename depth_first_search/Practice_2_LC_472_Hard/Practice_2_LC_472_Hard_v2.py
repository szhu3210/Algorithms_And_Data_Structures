class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                if (word[:i] in d) and ((word[i:] in d) or dfs(word[i:])):
                    return True
            return False
        return [word for word in words if dfs(word)]
