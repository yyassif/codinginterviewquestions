#Myungho Sim
#single number problem @ leetcode  - using hashmap
#25% better than other submissions. needs improvement
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}
        size = len(nums)
        for i in range(size):
            try:
                val = map[nums[i]]
                map[nums[i]] = val+1
            except:
                map[nums[i]] = 1
        for k,v in map.items():
            if v==1:
                return k
        return None
        
