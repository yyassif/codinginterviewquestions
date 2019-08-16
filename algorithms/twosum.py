#Myungho Sim
#more efficient solution using one pass hash table
# idea taken from https://medium.com/@havbgbg68/leetcode-1-two-sum-python-8d77c223abd3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        map = {}
        for i in range(0, size):
            diff = target-nums[i]
            if diff in map:
                return [map[diff],i]
            map[nums[i]]=i
        return None
            
# #brute force solution 
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         size = len(nums)
#         for i in range(0, size):
#             for j in range(i+1, size):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]
#         return None

