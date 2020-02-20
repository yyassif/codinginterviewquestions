#my own sol for design hit counter problem - run time better than 92%, 100% memory
#idea: improve by storing (timestamp, cnt) pair to array and binary search timestamp-300 and timestamp itself
class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr =[]
    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.arr.append(timestamp)
    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        count=0
        for t in self.arr:
            if timestamp-300<t<=timestamp:
                count+=1
        return count
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
