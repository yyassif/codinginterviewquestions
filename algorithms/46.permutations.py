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
    
                
#leetcode's solution   
#46. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def back(first=0):
            if first == n:
                ret.append(nums[:]) #copy of the whole array. Important! without[:] does not work
            for i in range(first, n):
                nums[first], nums[i] = nums[i],nums[first]
                back(first+1)
                nums[first], nums[i] = nums[i],nums[first]
        ret = []
        n = len(nums)
        back()
        return ret
            
