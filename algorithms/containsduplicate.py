#Myungho Sim
#contains duplicate question at leetcode using hash map
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = len(nums)
        m = {}
        for i in range(s):
            n = nums[i]
            try:
                val = m[n]
                if val==1:
                    return True
            except:
                m[n] = 1
        return False
