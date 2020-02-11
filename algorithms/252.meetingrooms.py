#252.meetingrooms.py
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
        
