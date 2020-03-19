# examples
# [[1,2], [4,5]] + 3 -> merge two intervals into [[1,5]]
# [[1,2], [5,6]] + 3 -> update [1,2] to [1,3]
# [[1,2], [5,6]] + 4 -> update [5,6] to [4,6]
# [[1,2], [6,7]] + 4 -> add another interval [4,4]

# cases 
# i = 0
# i = len(list)
# i in middle but need to merge with i-1
# i in middle but need to merge with original i
# i in middle but need to merge with original i and i-1
# i in middle but don't need to merge anything
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
        elif i == 0:  #leftmost
            if self.int[i][0] == val + 1:
                self.int[i][0] = val
            else:
                self.int.insert(i, [val, val])
        elif i == len(self.int):  #rightmost
            if self.int[i-1][1] == val - 1:  #check if new val can be merged w/ last interval. 
                self.int[i-1][1] = val
            else:
                self.int.append([val, val])
        elif self.int[i-1][1] == val - 1:     # e.g. [1,2],[4,4] and val =3
            self.int[i-1][1] = val
            if self.int[i][0] == val + 1: #check next interval since new val has been added and merge
                self.int[i-1][1] = self.int[i][1]
                self.int.pop(i)
        elif self.int[i][0] == val + 1: #update ith interval  e.g. [1,2] [6,6] and val=5
            self.int[i][0] = val
        else:
            self.int.insert(i, [val, val])
        
        self.table.add(val)
                
    def getIntervals(self):
        return self.int
