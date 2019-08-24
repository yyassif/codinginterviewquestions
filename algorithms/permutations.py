#Myungho Sim
#Implement permutation from Leetcode
#recursive solution taken from leetcode discussions
#solution also available at https://docs.python.org/3.7/library/itertools.html#itertools.permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ret =[]
        if l==0:
            return []
        if l==1:
            return [nums]
        for i in range(l):
            nums[0],nums[i] = nums[i],nums[0]
            for j in self.permute(nums[1:]):
               ret.append([nums[0]]+j)  #[nums[0]]+j is a python slice
            nums[0],nums[i] = nums[i],nums[0]
        return ret
    
                
            
