class Solution:
    def uniquePathsWithObstacles(self, ob_grid: List[List[int]]) -> int:
        nr = len(ob_grid)
        nc = len(ob_grid[0])
        if ob_grid[0][0]==1 or ob_grid[nr-1][nc-1]==1:
            return 0
        grid = [[0]*nc]*nr
        grid[0][0]=1
        def get_value(i,j):
            if 0<=i<nr and 0<=j<nc and ob_grid[i][j]==0:
                return grid[i][j]
            else:
                return 0
            
        for i in range(nr):
            for j in range(nc):
                if i==0 and j==0:
                    continue
                grid[i][j] = get_value(i,j-1)+get_value(i-1,j)
        return grid[nr-1][nc-1]
