approach 1: backtracking run- O(2^n) , space - O(n)
Approach 2: Dynamic Programming Top-down run- bottom up/top down O(n^2)
Approach 2: greedy - runtime O(n)

https://leetcode.com/problems/jump-game/discuss/606056/Py3-Sol%3A-Greedy-Bottom-Up-Top-down-Easy-to-Understand
# Below is the top-down approach

def Jump(nums, dp, ind):
    if nums[0]>=len(nums) or (nums[0]==0 and len(nums)==1): return True # [0] case
    if nums[0]==0: return False
    if dp[ind]!=None:
        print("dp used")
        return dp[ind]
    status = True
    for i in range(1, nums[0]+1):
        if i==1:
            status = Jump(nums[i:], dp, ind + i)
        else:
            status = status or Jump(nums[i:], dp, ind + i)
    dp[ind] = status
    return dp[ind]


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        t = list(set(nums))
        if len(t)==1 and t[0]>=1: return True
        dp = [None]*len(nums)
        return Jump(nums, dp, 0)

# --------------------------------------------------------------
# Below is the bottom-up approach

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[-1] = True
        for i in range(len(nums)-2,-1,-1):
            n = nums[i]
            if n==0:
                dp[i]=False
                continue
            for j in range(n, 0,-1): # [n,1] inclusive
                if i+j<len(dp) and dp[i+j]==True:
                    dp[i] = True
                    break
        # print(dp)
        return dp[0]

# ----------------------------------------------------------------
# Below is the greedy approach

class Solution:
    def canJump(self, nums):
        leftMostGoodJumpIndex = len(nums)-1 # it will be always True,
        # since destination is here
        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= leftMostGoodJumpIndex:
                # yes, leftMostGoodJumpIndex is in range of current pos
                # so current index will also be a leftMostGoodJumpIndex
                leftMostGoodJumpIndex = i
        return leftMostGoodJumpIndex==0
