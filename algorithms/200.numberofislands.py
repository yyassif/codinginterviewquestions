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
                
#version 2 - my own bfs solution. 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr=len(grid)
        if nr==0:
            return 0
        nc = len(grid[0])
        if nc==0:
            return 0
        q= []
        lands = []
        #find land
        for i in range(nr):
            for j in range(nc):
                grid[i][j]=int(grid[i][j])
                if grid[i][j]==1:
                    lands.append((i,j))
        dirs= {(0,-1), (0,1), (1,0),(-1,0)}
        def valid(a,b):
            if 0<=a<nr and 0<=b<nc and grid[a][b]==1:
                return True
            return False
        
        def bfs(a,b):
            q.append((a,b))
            while q:
                x,y = q.pop(0)
                for direc in dirs:
                    if valid(x+direc[0], y+direc[1]):
                        q.append((x+direc[0], y+direc[1]))
                        grid[x+direc[0]][y+direc[1]]=2 #mark as visited
        ret=0
        for land in lands:
            a,b = land
            if grid[a][b]==1:
                bfs(a,b)
                ret+=1
        return ret
        
