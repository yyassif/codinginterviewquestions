#980. Unique Paths III 
# dynamic programming sol is hard to understand. 
# Use the DFS back tracking sol
class Solution:
    def uniquePathsIII(self, grid):
        R, C = len(grid), len(grid[0])

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0: #check valid & unvisited path
                    # mod 2 to include end tile, 0=empty tile
                    yield nr, nc

        todo = 0 #unvisited empty tiles
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1: todo += 1
                if val == 1: sr, sc = r, c  #start
                if val == 2: tr, tc = r, c  #end

        self.ans = 0
        def dfs(r, c, todo): #recursive DFS
            todo -= 1
            if todo < 0: return
            if r == tr and c == tc: #end reached
                if todo == 0: #all tiles visited
                    self.ans += 1  #increment # of paths from Start to end
                return

            grid[r][c] = -1 #mark as visited
            for nr, nc in neighbors(r, c):
                dfs(nr, nc, todo)
            grid[r][c] = 0 #mark back as unvisited to get different path

        dfs(sr, sc, todo) #start from 
        return self.ans
