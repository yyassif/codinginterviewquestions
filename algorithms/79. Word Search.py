#recursive dfs sol
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nr=len(board)
        if nr==0:
            return False
        nc = len(board[0])
        if nc==0:
            return False
        visited=set()
        def bfs(a,b,idx):
            if idx==len(word):
                return True
            if 0<=a<nr and 0<=b<nc and (a,b) and board[a][b]!="#" \
                and board[a][b]==word[idx]:
                temp = board[a][b]
                board[a][b] = "#"
                result =  False or bfs(a+1,b,idx+1) or bfs(a-1, b, idx+1)\
                    or bfs(a,b-1,idx+1) or bfs(a,b+1,idx+1)
                board[a][b] = temp
                return result
        for i in range(nr):
            for j in range(nc):
                if board[i][j]==word[0]: #matches starting letter
                    visited=set()
                    result = bfs(i,j,0)
                    if result:
                        return result
        return False
                    
                    
                    
                    
