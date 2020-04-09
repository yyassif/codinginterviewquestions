#binary search
from bisect import bisect_left 
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cnt=1
        self.map = {}

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp not in self.map:
            self.map[timestamp] = 1
        else:
            self.map[timestamp] +=1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        #search for start
        
        times = list(self.map)
        start_idx = bisect_left(times, timestamp-299 if timestamp-299>0 else 0)
        if start_idx==len(times): #no hits past 5 minutes
            return 0
        try:
            start_time = times[start_idx]
        except:
            print("ex:",start_idx, "t",timestamp)
            
        curr_idx = bisect_left(times, timestamp)
        if curr_idx==len(times):
            curr_idx-=1
        sumv =0
        for i in range(start_idx, curr_idx+1):
            key = times[i]
            sumv += self.map[key]
        return sumv
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

#my own sol for design hit counter problem - run time better than 92%, 100% memory
#idea: improve by storing (timestamp, cnt) pair to array and binary search timestamp-300 and timestamp itself
# low=t-299 and high=timestamp, binary search idx low and high. count numbers between low and high
# refer to https://leetcode.com/problems/design-hit-counter/discuss/500382/python-binary-search-solution for 2nd sol
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
