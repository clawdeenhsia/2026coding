#week02-3.py
#leetcode 392
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # s 的指標
        j = 0  # t 的指標

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
