class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        if n==0:
            return intervals
        i=0
        intervals.sort(key=lambda x:(x[0],x[1]))
        while i<n-1:
            s = intervals[i][0]
            e = intervals[i][1]
            sn = intervals[i+1][0]
            en = intervals[i+1][1]
            print(i,intervals)
            while i<n-1 and e>=sn:
                intervals[i][1] = en if en>e else e
                del intervals[i+1]
                n-=1
                if i<n-1:
                    s = intervals[i][0]
                    e = intervals[i][1]
                    sn = intervals[i+1][0]
                    en = intervals[i+1][1]
                else:
                    break
            i+=1
        return intervals
            
            
