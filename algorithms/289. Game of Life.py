# uses a copy of matrix space/runtime O(M*N)
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m==0:
            return board
        n = len(board[0])
        if n==0:
            return board
        def valid(a,b):
            if 0<=a<m and 0<=b<n:
                return True
        mat = [row[:] for row in board] #original copy of the board
        directions = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
        for i in range(m):
            for j in range(n):
                #count how many live=1 or dead=0 cells surrounding cell (i,j)
                cnt_live=0
                for direc in directions:
                    if valid(i+direc[0],j+direc[1]):
                        if mat[i+direc[0]][j+direc[1]]==1:
                            cnt_live+=1
                if mat[i][j]==1 and cnt_live<2 or mat[i][j]==1 and cnt_live>3:
                    board[i][j]=0
                elif mat[i][j]==1 and 2<=cnt_live<=3 or mat[i][j]==0 and cnt_live==3:
                    board[i][j]=1
