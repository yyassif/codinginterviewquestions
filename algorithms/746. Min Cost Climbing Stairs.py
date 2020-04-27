#dynamic programming , backward, space O(1), run O(n)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        f1 = f2 = 0
        for x in reversed(cost): #work backwards in the list
            f1, f2 = x + min(f1, f2), f1   #add new value to the minimum and swap
        return min(f1, f2)

#dynamic programming, forward, space and runtime - O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        arr = [0 for i in range(n)]
        arr[0] = cost[0]
        arr[1] = cost[1]
        for i in range(2,n):
            arr[i] = min(arr[i-1]+cost[i], arr[i-2]+cost[i])
        return min(arr[-1],arr[-2])
            
