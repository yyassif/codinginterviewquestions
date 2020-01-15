# 295. Find Median from Data Stream - Hard
# brute force solution
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        n = len(self.arr)
        m = n//2
        if n%2==0:
            return (self.arr[m-1]+self.arr[m])/2
        else:
            return self.arr[m]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
