#week03-2.py
#Leetcode 643
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N=len(nums)
        total=sum(nums[:k])
        maxTotal=total
        for i in range(k,N):
            total=total+nums[i]-nums[i-k]
            #num[i]右邊的頭(往右吃)nums[i-k]左邊的尾 吐出來
            maxTotal=max(maxTotal,total)
        return maxTotal/k
