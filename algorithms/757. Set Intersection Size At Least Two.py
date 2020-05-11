#greedy sol https://leetcode.com/problems/set-intersection-size-at-least-two/discuss/439986/Python-keep-track-of-the-right-most-2-points
#Sort intervals by end. The right-most 2 points are the one we are interested in.
#When a new interval comes, reuse the current right-most 2 points as much as possible.
#If can't reuse, then introduce new points to the right-most side of new interval.
class Solution(object):
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        res =0
        s,e=0,0 #start, end
        isNew=True
        for start, end in intervals:
            # at the start OR temp start,end = 5,7, temp s,e: 1,3 => temp s,e=6,7
            if isNew==True or start>e:
                res+=2
                s=end-1
                e=end
                isNew=False
            # temp s,e = 1,3, interval: 2,4 => temp s,e=3,4
            elif start>s:
                res+=1
                s= e
                e= end
        return res
    
#https://leetcode.com/problems/set-intersection-size-at-least-two/discuss/279406/Python-O(nlogn)-always-peek-the-top-two-elements-of-maxheap
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
