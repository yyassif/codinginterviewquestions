#backtracking sol
#run time  O(N*N!), space O(n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        ret=[]
        def back(first=0):
            if first==n:
                ret.append(nums[:])
            for i in range(first, n):
                nums[first],nums[i] = nums[i], nums[first]
                back(first+1)
                nums[first],nums[i] = nums[i], nums[first]
                
        back()
        return ret
