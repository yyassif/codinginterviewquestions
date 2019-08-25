# Myungho Sim
# Majority Element problem at leetcode using hash map
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for n in nums:
            try:
                val = map[n]
                map[n] = val+1
            except:
                map[n]=1
        for k,v in map.items():
            print(k,v)
            if v>= len(nums)/2:
                return k
        return None
