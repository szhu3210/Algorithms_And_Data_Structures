class Solution:

    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        res = [1, 0, 0]
        def expand(i , j):
            while i-1 >= 0 and j+1 < l and s[i-1] == s[j+1]:
                i -= 1
                j += 1
            length = j - i + 1
            if length > res[0]:
                res[:] = [length, i, j]
        for c in range(l):
            i = j = c
            expand(i, j)
            if c + 1 < l and s[c] == s[c+1]:
                i, j = c, c + 1
                expand(i, j)
        length, i, j = res
        return s[i: j + 1]
