#run O(n), space=O(1) sol
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
