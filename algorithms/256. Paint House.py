#input : nth row represents costs for col 0=red, col 1=blue, col 2 =green for the nth row house.
#dynamic programming - bottom up. O(n) space and runtime
#for any number of colors and houses
#faster if you remove inner for loops and manually set values for 3 colors
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if costs==[]:
            return 0
        for i in reversed(range(len(costs)-1)):
            for j in range(len(costs[0])):
                mini=float('inf')
                for k in range(len(costs[0])):
                    if j==k:
                        continue
                    mini = min(costs[i+1][k],mini)
                costs[i][j]+=mini
        print(costs)
        return min(costs[0])
            
        
#memoization, recursive method: runtime- O(n), space- O(n)
from functools import lru_cache
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        self.memo={}
        if costs == []:
            return 0
        @lru_cache(None)
        def helper(row, color):
            if (row, color) in self.memo:
                return self.memo[(row,color)]
            sumv = costs[row][color]
            if row==len(costs)-1:
                return sumv
            min_val=float('inf')
            for i in range(len(costs[0])):
                if i==color:
                    continue
                min_val=min(min_val,helper(row+1,i))
            sumv+=min_val
            self.memo[(row,color)]=sumv
            return self.memo[(row,color)]
        return min(helper(0,0),helper(0,1),helper(0,2))
    
##################################################################
#brute force time limit exceeded 22 / 101 test cases passed.
#runtime O(2^n) space -O(n)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if costs == []:
            return 0
        def helper(row, color):
            sumv = costs[row][color]
            if row==len(costs)-1:
                return sumv
            min_val=float('inf')
            for i in range(len(costs[0])):
                if i==color:
                    continue
                min_val=min(min_val,helper(row+1,i))
            sumv+=min_val
            return sumv
        return min(helper(0,0),helper(0,1),helper(0,2))
