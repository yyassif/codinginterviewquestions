#Myungho Sim
#remove duplicates from sorted array from leetcode.
#faster than 99% of submissions
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        curIdx=1
        for i in range(size):
            if i==0:
                continue
            if nums[i]!=nums[i-1]:
                nums[curIdx] = nums[i]
                curIdx+=1
        return curIdx
