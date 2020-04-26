#input : nth row represents costs for col 0=red, col 1=blue, col 2 =green for the nth row house.
#brute force time limit exceeded 22 / 101 test cases passed.
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
