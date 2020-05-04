https://leetcode.com/discuss/interview-question/344677
Input: ropes = [8, 4, 6, 12]
Output: 58
Explanation: The optimal way to connect ropes is as follows
1. Connect the ropes of length 4 and 6 (cost is 10). Ropes after connecting: [8, 10, 12]
2. Connect the ropes of length 8 and 10 (cost is 18). Ropes after connecting: [18, 12]
3. Connect the ropes of length 18 and 12 (cost is 30).
Total cost to connect the ropes is 10 + 18 + 30 = 58
Example 2:

Input: ropes = [20, 4, 8, 2]
Output: 54
Example 3:

Input: ropes = [1, 2, 5, 10, 35, 89]
Output: 224
Example 4:

Input: ropes = [2, 2, 3, 3]
Output: 20


from heapq import heappop, heappush, heapify
def minCost(ropes):
    if not ropes:
        return 0
    if len(ropes) == 1:
        return ropes[0]
    heapify(ropes)
    cost = 0
    while len(ropes) > 1:
        a, b = heappop(ropes), heappop(ropes)
        cost += a+b
        if ropes:
            heappush(ropes, a+b)
    return cost

#test drivers
ropes = [8, 4, 6, 12]
print(ropes)
ret= minCost(ropes)
print("expected:58")
print(ret)


ropes = [20, 4, 8, 2]
print(ropes)
ret= minCost(ropes)
print("expected:58")
print(ret)

ropes = [1, 2, 5, 10, 35, 89]
print(ropes)
ret= minCost(ropes)
print(ret)
print("expected:224")

ropes = [2, 2, 3, 3]
print(ropes)
ret= minCost(ropes)
print("expected:20")
print(ret)

##########################################################################
#sol 2 
import heapq
def minCost(sticks):
    heapq.heapify(sticks)
    ans = 0
    while len(sticks) >= 2:
        ncost = heapq.heappop(sticks) + heapq.heappop(sticks)
        heapq.heappush(sticks, ncost)
        ans += ncost

    return ans
