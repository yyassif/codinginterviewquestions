#Myungho Sim
#find the duplicate number @leetcode
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        arr = [0]*(size+1)
        for n in nums:
            if arr[n]==1:
                return n
            else:
                arr[n] = 1
        return -1
