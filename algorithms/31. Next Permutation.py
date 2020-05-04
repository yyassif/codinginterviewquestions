#video tutorial
https://www.youtube.com/watch?v=PYXl_yY-rms
# e.g. 123
# 123
# 132  #reverse numbers after 1
# 213
# 231
# 312
# 321  <- all numbers are in decreasing order
# [algorithm]
1) find the first decreasing number when going backwards from the back. 1247651 <--4
2) swap with the number with the largest decrease. (or a number just larger than the number from step)
12476*5*1   <--5 in this case. swap with 4
1257641
3) reverse all numbers after 5
1251467
#from https://leetcode.com/problems/next-permutation/discuss/14054/Python-solution-with-comments.
def nextPermutation(self, nums):
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:  #find the first idx of decreasing # when going backwards
        i -= 1                             #e.g. 847531  <--i=2 ,4 is the number @i-1=1, i=2 is 7
    if i == 0:   # nums are in descending order
        nums.reverse()
        return 
    k = i - 1    # find the last "ascending" position
    while nums[j] <= nums[k]:
        j -= 1
    nums[k], nums[j] = nums[j], nums[k]  
    l, r = k+1, len(nums)-1  # reverse the second part
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1 ; r -= 1
#my interpretation of the same code from above
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #find first increasing
        n=len(nums)
        inc_idx=n-1
        while inc_idx>0 and nums[inc_idx-1]>=nums[inc_idx]:
            inc_idx-=1
        if inc_idx==0:
            nums.reverse()
            return
        #find the last number larger than first increasing num = last ascending pos
        last_idx=n-1
        #e.g. 847531 starting at end, going backwards, find the first number larger than nums[inc_idx]
        while nums[last_idx]<=nums[inc_idx-1]:  
            last_idx-=1
        
        nums[inc_idx-1],nums[last_idx] = nums[last_idx],nums[inc_idx-1]
        #reverse numbers after
        i=inc_idx
        j=n-1
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        
