# 295. Find Median from Data Stream - Hard
# binary search sol
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.n=0
    def addNum(self, num: int) -> None:
        def binarySearch(t): #return index where num can be inserted
            l=0
            r=len(self.arr)-1
            m = -1
            while l<=r:
                m = (l+r)//2
                # if t==self.arr[m]:
                #     return m
                if self.arr[m]>=t:
                    r=m-1
                else:
                    l=m+1
            return l
        self.arr.insert(binarySearch(num),num)
        self.n+=1

    def findMedian(self) -> float:
        m = self.n//2
        if self.n%2==0:
            return (self.arr[m-1]+self.arr[m])/2
        else:
            return self.arr[m]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

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
