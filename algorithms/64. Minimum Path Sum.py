#study both 2d and 1d methods run-O(M*N)  space O(M)
#1d method
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n==0 or m==0:
            return 0
        dp = [0 for _ in range(m)]
        for i in range(n-1,-1,-1):
            for j in range(m-1, -1,-1):
                if i==n-1 and j!=m-1:  #last row of grid
                    dp[j] = grid[i][j]+dp[j+1]
                elif j==m-1 and i!=n-1: #last col of grid
                    dp[j] = grid[i][j]+dp[j]
                elif j!=m-1 and i!=n-1:
                    dp[j] = grid[i][j]+min(dp[j],dp[j+1])
                else:
                    dp[j] = grid[i][j]
        return dp[0]

#2d method run/space-O(M*N)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        memo = [[0]*nc]*nr
        def get_val(i,j):
            if 0<=i<nr and 0<=j<nc:
                return grid[i][j]
            else:
                return float('inf')
        for i in reversed(range(nr)):
            for j in reversed(range(nc)):
                if i==nr-1 and j!=nc-1:
                    grid[i][j] += grid[i][j+1]
                elif i!=nr-1 and j==nc-1:
                    grid[i][j] += grid[i+1][j]
                elif i!=nr-1 and j!=nc-1:
                    grid[i][j] += min(grid[i][j+1], grid[i+1][j])
        return grid[0][0]
