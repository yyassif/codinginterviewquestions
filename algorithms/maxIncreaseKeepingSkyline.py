#Myungho Sim
#max increase to keep city skyline @leetcode
#faster than 99% of submissions
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        size = len(grid)
        tb =[] #top to bottom skyline
        lr = [] #left to right skyline
        tbmax=0
        lrmax=0
        for i in range(size):
            lrmax=0
            for j in range(size):
                if lrmax<grid[i][j]:
                    lrmax = grid[i][j]
            lr.append(lrmax)
        for i in range(size):
            tbmax=0
            for j in range(size):
                if tbmax<grid[j][i]:
                    tbmax = grid[j][i]
            tb.append(tbmax)
        cnt=0
        diff=0
        h=0
        print (tb)
        print (lr)
        for i in range(size):
            for j in range(size):
                if tb[j]>lr[i]:
                    h = lr[i]
                else:
                    h = tb[j]
                if grid[i][j]<h:
                    diff = abs(grid[i][j]-h)
                    cnt += diff
        return cnt
