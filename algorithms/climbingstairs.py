#Myungho Sim
#climbing stairs problem at leetcode
#same as nth fibonacci sequence problem. solved using dynamic programming.
class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0]*(n+1)
        arr[0]=1
        arr[1]=1
        if n==0 or n==1:
            return arr[n-1]
        for i in range(2,n+1):
            arr[i] = arr[i-1]+arr[i-2]
        return arr[n]
