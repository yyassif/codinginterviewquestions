class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = collections.deque()
        nr = len(grid)
        if nr==0:
            return -1
        nc = len(grid[0])
        def checkFreshRemaining():
            for i in range(nr):
                for j in range(nc):
                    if grid[i][j]==1:
                        return True
            return False
        #find and add rotten oranges
        for i in range(nr):
            for j in range(nc):
                if grid[i][j]==2:
                    que.append((i,j,0))
        def checkFresh(i,j):
            if i>=0 and i<nr and j>=0 and j<nc and grid[i][j]==1:
                return True
            else:
                return False
        depth=0
        cnt=0
        while que:
            ri,ci,depth = que.popleft()
            if checkFresh(ri-1,ci):
                que.append((ri-1,ci,depth+1))
                grid[ri-1][ci]=2
            if checkFresh(ri+1,ci):
                que.append((ri+1,ci,depth+1))
                grid[ri+1][ci]=2
            if checkFresh(ri,ci-1):
                que.append((ri,ci-1,depth+1))
                grid[ri][ci-1]=2
            if checkFresh(ri,ci+1):
                que.append((ri,ci+1,depth+1))
                grid[ri][ci+1]=2
        if checkFreshRemaining()==False:
            return depth
        return -1
