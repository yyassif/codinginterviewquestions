# best sol @ https://leetcode.com/problems/data-stream-as-disjoint-intervals/discuss/542911/Python-binary-search-and-insert-remove-merge-element
class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.int = []
        self.table = set()
        
    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        def bisect_left(arr, val):
            l = 0
            r = len(arr)
            while l < r:
                m = l + (r-l) // 2
                if arr[m][0] > val:
                    r = m
                else:
                    l = l + 1
            return l

        if val in self.table:
            return
        i = bisect_left(self.int, val)
        if not self.int:
            self.int.append([val, val])
        elif i == 0:
            if self.int[i][0] == val + 1:
                self.int[i][0] = val
            else:
                self.int.insert(i, [val, val])
        elif i == len(self.int):
            if self.int[i-1][1] == val - 1:
                self.int[i-1][1] = val
            else:
                self.int.append([val, val])
        elif self.int[i-1][1] == val - 1:
            self.int[i-1][1] = val
            if self.int[i][0] == val + 1:
                self.int[i-1][1] = self.int[i][1]
                self.int.pop(i)
        elif self.int[i][0] == val + 1:
            self.int[i][0] = val
        else:
            self.int.insert(i, [val, val])
        
        self.table.add(val)
                
    def getIntervals(self):
        return self.int
