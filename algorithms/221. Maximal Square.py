#sol based on https://leetcode.com/articles/maximal-square/
#find max SQUARE AREA. NOT a rectangle. just find max width 
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        if r==0:
            return 0
        c = len(matrix[0])
        if c==0:
            return 0
        prev=0
        dp = [0 for _ in range(c+1)]
        maxw=0
        #dp[j] is UP, dp[j-1]=LEFT, prev is Diagonal/Upper left. 
        for i in range(1, r+1):
            for j in range(1, c+1):
                temp = dp[j]
                if matrix[i-1][j-1]=="1":
                    dp[j] = min(dp[j], dp[j-1], prev)+1
                    maxw = max(maxw, dp[j])  #update max width
                else:
                    dp[j] = 0
                prev=temp
        return maxw**2
