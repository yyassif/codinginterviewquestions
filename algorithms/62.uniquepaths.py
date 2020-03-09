#62.uniquepaths.py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr =[[0]*n]*m #m rows , n cols
        for i in range(n):
            arr[0][i] = 1
        for i in range(m):
            arr[i][0] = 1
        def isValid(x,y):
            return 0<=x<=m and 0<=y<=n
        for i in range(1,m):
            for j in range(1,n):
                up=0
                left=0
                if isValid(i-1,j):
                    up = arr[i-1][j]
                if isValid(i,j-1):
                    left = arr[i][j-1]
                print(i,j, i-1, j, i, j-1, up, left)
                arr[i][j] = up+left
        print(arr)
        return arr[m-1][n-1]
        
