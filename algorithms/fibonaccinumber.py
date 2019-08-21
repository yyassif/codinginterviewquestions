#Myungho Sim
#solution for fibonacci number using hashmap. beats 90% of submissions on leetcode
class Solution:
    def fib(self, N: int) -> int:
        map = {}
        if N==0:
            return 0
        elif N==1:
            return 1
        map[0]=0
        map[1]=1
        for i in range(2,N+1):
            v = map[i-2]+map[i-1]
            map[i] = v
        return map[N]
