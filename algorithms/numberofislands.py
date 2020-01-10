#Myungho Sim
# No 200 number of islands problem at leetcode
# DFS solution similar to leetcode's
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid,r,c):
            nr = len(grid)
            nc = len(grid[0])
            if (r<0 or c<0 or r>=nr or c>=nc or grid[r][c]=="0"):
                return
            grid[r][c] = "0"
            dfs(grid,r+1,c) #visit one cell up
            dfs(grid,r-1,c) # visit down
            dfs(grid,r,c+1) # visit right
            dfs(grid,r,c-1) #visit left
            
        if len(grid)==0 or grid is None:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        cnt=0 #count islands
        for i in range(nr):
            for j in range(nc):
                if grid[i][j]=="1":
                    cnt+=1
                    dfs(grid, i,j)
        return cnt
                
