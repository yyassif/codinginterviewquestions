class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0,curr,p2 = 0,0,len(nums)-1
        while curr<=p2:  #when curr is at p2, you still want to compare with p1. p2 is at left boundary of 2's.
            if nums[curr]==0:
                nums[curr],nums[p0] = nums[p0],nums[curr]
                curr+=1
                p0+=1
            elif nums[curr]==2:
                nums[curr],nums[p2] = nums[p2],nums[curr]
                curr+=1
                p2-=1
            else:
                p1+=1
        return nums
