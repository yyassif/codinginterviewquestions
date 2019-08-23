#Myungho Sim
#get kth element from back from leetcode
#solution using max heap. beats 80~98%
class Solution: 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr =[]
        for n in nums:
            arr.heappush(n)
        for i in k-1:
            arr.heappop()
        return arr.heappop()
#solution beats 80~93%
class Solution: 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[::-1][k-1]
