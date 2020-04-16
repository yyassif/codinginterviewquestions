# most efficient run O(n), space=O(1) sol
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        j=0
        for i in range(n):
            if nums[i]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
####################################################
#suboptimal run O(n), space=O(1) sol
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        n=len(nums)
        for j in range(n):
            if nums[j]!=0:
                nums[i] = nums[j]
                i+=1
        while i<n:
            nums[i]=0
            i+=1
