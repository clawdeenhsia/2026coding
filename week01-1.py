#week01-1.py
#Leetcode 1404
class Solution:
    def numSteps(self, s: str) -> int:
        ans=0 #羆璶ǐ碭˙
        n = int(s,2)  #р﹃S讽秈俱计跑ΘN
        while n>1:  #ヘ夹:n程穦跑Θ1
            if n%2==0: n=n//2 #案计//2
            else: n=n+1  #计+1
            ans += 1
        return ans #羆璶ǐ碭˙
