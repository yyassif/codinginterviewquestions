#Myungho Sim
#missing number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        arr = [-1] * (size+1)
        for i in range(size):
            arr[nums[i]]=1
        try:
            num = arr.index(-1)
        except:
            num=-1
        return num
