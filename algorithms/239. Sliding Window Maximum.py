# Python solution using heap and deque
# https://leetcode.com/problems/sliding-window-maximum/discuss/565554/Python-solution-using-heap-and-deque
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [(-nums[i],i) for i in range(k-1)]
        heapq.heapify(q)
        maxs = []
        for i,num in enumerate(nums[k-1:],k-1):
            heapq.heappush(q,(-num,i))
            maxs.append(self.get_max_gt_start(q,i-k+1))
        return maxs
    
    def get_max_gt_start(self, q, start):
        while True:
            val, indx = q[0]
            if indx >= start:
                return -val
            heapq.heappop(q)
Adding the deque version as well.

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        maxs =[]
        for i, num in enumerate(nums):
            # if element at the top of queue is smaller, we don't need it
            while q and q[-1][0] < num:
                q.pop()
            #push the current element onto stack
            q.append((num,i))
            
            #find the max from other end of the queue
            if i >= k -1:
                if q[0][1] < i-k+1:
                    q.popleft()
                maxs.append(q[0][0])
        
        return maxs
