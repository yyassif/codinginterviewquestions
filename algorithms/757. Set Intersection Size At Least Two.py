class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1])
        hp = []
        heapq.heappush(hp, -intervals[0][1])
        heapq.heappush(hp, -intervals[0][1]+1)
        for i in range(1, len(intervals)):
            t1 = -heapq.heappop(hp)
            t2 = -heapq.heappop(hp)
            if not intervals[i][0]<=t1<=intervals[i][1]:
                heapq.heappush(hp, -intervals[i][1])
                if not intervals[i][0]<=t2<=intervals[i][1]:
                    heapq.heappush(hp, -intervals[i][1]+1)
            else:
                if not intervals[i][0]<=t2<=intervals[i][1]:
                    heapq.heappush(hp, -intervals[i][1])
            heapq.heappush(hp, -t1)
            heapq.heappush(hp, -t2)
        return len(hp)
