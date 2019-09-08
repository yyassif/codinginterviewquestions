#Myungho Sim
#378. Kth Smallest Element in a Sorted Matrix @leetcode
import sys
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m=0
        prev=-sys.maxsize-1 #prev matrix cell
        cnt=1
        ret = []
        for i in range(0,n):
            for j in range(0,n):
                m = matrix[i][j]
                ret.append(m)
        ret.sort()
        return ret[k-1]
                
            
