#week01-2.py
#Leetcode 1768
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans="" #答案在ans裡
        N1, N2=len(word1),len(word2)
        i, j=0,0 #word[i] vs. word2[j]
        while i<N1 or j<N2: #只要任一個還有剩
            if i<N1: ans+= word1[i]
            if j<N2: ans+= word2[j]
            i,j = i+1,j+1
        return ans #答案在這裡
