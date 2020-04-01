#240. Search a 2D Matrix II
#Most efficient O(n+m) solution
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nr=len(matrix)
        if nr==0:
            return False
        nc=len(matrix[0])
        if nc==0:
            return False
        r=nr-1
        c=0
        while r>=0 and c<nc:
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                c+=1
            elif matrix[r][c]>target:
                r-=1
        return False
        
