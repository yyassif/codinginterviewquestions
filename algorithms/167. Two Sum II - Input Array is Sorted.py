class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        visited=set()
        l=0
        r=n-1
        while l<=r:
            sum =nums[l]+nums[r]
            if sum==target:
                return [l+1,r+1]
            elif sum<target:
                l+=1
            elif sum>target:
                r-=1
        return []
