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
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
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
