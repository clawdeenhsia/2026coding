#week13-4.py
#leetcode 2336D
class SmallestInfiniteSet:

    def __init__(self):
        self.now=0
        self.heap=[]


    def popSmallest(self) -> int:
        if self.heap:
            return heappop(self.heap)
        self.now+=1
        return self.now

    def addBack(self, num: int) -> None:
        if num<self.now:
            heappush(self.heap,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
