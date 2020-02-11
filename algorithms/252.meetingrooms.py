#252.meetingrooms.py
#sorting - o(nlogn)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda intervals:intervals[0])
        for i in range(len(intervals)-1):
            end1 = intervals[i][1]
            start2 = intervals[i+1][0]
            if end1>start2:
                return False
        return True
        
        
#brute force
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        size = len(intervals)
        map = {}
        for slot in intervals:
            start, end  = slot
            for i in range(start, end+1):
                if i in map:
                    if i==start and map[i]=="e":
                        pass
                    elif i==end and map[i]=="s":
                        pass
                    else:
                        return False
                else:
                    if i==start:
                        map[i] = "s"
                    elif i==end:
                        map[i] = "e"
                    else:
                        map[i] = 1
        return True
        
