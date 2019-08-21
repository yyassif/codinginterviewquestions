#Myungho Sim
#single number problem @ leetcode  - using hashmap
#25% better than other submissions. needs improvement
#this is better than brute force method which loop over the number for each digit. In that case running time is O(n^2)
#using hash map, the running time is O(n)
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
        
