#Myungho Sim
#leetcode - remove element problem
#faster than 98%
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        curIdx = 0
        i=0
        while(i<size):
            if(nums[i]!=val):
                nums[curIdx] = nums[i]
                curIdx+=1 # curIdx for the next number to copy that doesn't match val
            i+=1
        return curIdx #size is already updated by curIdx+=1
            
