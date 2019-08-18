#Myungho Sim
#search insert position problem @leetcode
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        mid=0
        if(target<nums[0]):
            return 0
        elif (target>nums[high]):
            return high+1
        while(low<=high):
            mid = int((high+low)/2)
            if (nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                low = mid+1
            elif (nums[mid]>target):
                high = mid-1
        return low
        
