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
