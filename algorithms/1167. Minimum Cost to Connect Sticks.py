# 1167. Minimum Cost to Connect Sticks
# e.g. list= [2,4,3] -> [ 2,3,4]   cost_1= 2,3 is 5, 5+4=9,  total cost: 5+9=14
import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        heapq.heapify(sticks)
        while len(sticks)>1:
            sums = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost +=  sums
            heapq.heappush(sticks, sums)
        return cost
