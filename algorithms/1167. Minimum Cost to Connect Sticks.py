# 1167. Minimum Cost to Connect Sticks
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
