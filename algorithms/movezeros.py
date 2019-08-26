#Myungho Sim
#Move zeroes in place
#leetcode question
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        lastIdx=size-1 #last digit index where zero will be set
        i=0
        while i<lastIdx:
            if nums[i]==0:
                for j in range(i,lastIdx):
                    nums[j]=nums[j+1]
                nums[lastIdx]=0
                lastIdx-=1
            else:
                i+=1
                
