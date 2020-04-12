class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n<2:
            return n
        import heapq
        q=[]
        heapq.heapify(q)
        intervals.sort(key=lambda x:x[0])
        heapq.heappush(q,intervals[0][1])
        for i in range(1, n):
            if q[0]<=intervals[i][0]: 
                heapq.heappop(q)
            heapq.heappush(q, intervals[i][1])
        return len(q)
