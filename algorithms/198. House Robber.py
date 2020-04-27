class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        n = len(nums)
        dp = [0 for i in range(n)]
        maxi = dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
            maxi = max(maxi, dp[i])
        return maxi
            
