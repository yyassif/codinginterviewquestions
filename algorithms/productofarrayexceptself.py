#Myungho Sim
#ideas taken from leetcode solution using left and right arrays
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1,2,3,4]
        size = len(arr)
        L = [0]*size
        R = [0]*size
        L[0]=1
        for i in range(1,size):
            L[i] = arr[i-1]*L[i-1]
        R[size-1] = 1
        for i in reversed(range(size-1)):
            R[i] = arr[i+1]*R[i+1]
        ret = [0]*size
        for i in range(size):
            ret[i] = L[i]*R[i]
        return ret
