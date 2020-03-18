#Myungho Sim
#ideas taken from leetcode solution using left and right arrays
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L= [1]*n
        R= [1]*n
        arr=[1]*n
        for i in range(1,n):
            L[i] = nums[i-1]*L[i-1]
        for i in reversed(range(n-1)):
            R[i] = nums[i+1]*R[i+1]
        print(L)
        print(R)
        for i in range(n):
            arr[i] = L[i]*R[i]
        return arr
        
