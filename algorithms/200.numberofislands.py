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
                
#version 2 - my own bfs solution. runtime is better than 44%, memory usage is better than 91%
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr==0:
            return 0
        nc = len(grid[0])
        que =[]
        def checkValid(r,c):
            if 0<=r<nr and 0<=c<nc and grid[r][c]=='1':
                return True
            return False
        def bfs(grid,r,c):
            if r<0 or c<0 or r>=nr or c>=nc or grid[r][c]=='0':
                return
            que.append((r,c))
            while que:
                (r,c) = que.pop(0)
                if checkValid(r-1,c):
                    grid[r-1][c] = '0'
                    que.append((r-1,c))
                if checkValid(r+1,c):
                    grid[r+1][c] = '0'
                    que.append((r+1,c))
                if checkValid(r,c-1):
                    grid[r][c-1] = '0'
                    que.append((r,c-1))
                if checkValid(r,c+1):
                    grid[r][c+1] = '0'
                    que.append((r,c+1))
            
        cnt =0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    cnt +=1
                    bfs(grid,i,j)
        return cnt
                
        
