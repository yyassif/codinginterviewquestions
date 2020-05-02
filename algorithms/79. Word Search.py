#dfs and visited sol, recursive sol
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(word,i,j):
            if not word: # If we have seen all the matching characters in a word, we're done.
                return True
            else:
                if i < 0 or j < 0 or i > len(board)-1 or j > len(board[0])-1 or board[i][j] != word[0]:
                    return
                temp = board[i][j]
                board[i][j] = '#'
                result = False or dfs(word[1:],i+1,j) or dfs(word[1:],i-1,j) or dfs(word[1:],i,j-1) or dfs(word[1:],i,j+1) # we can also write len(word) == 0 in place of False
                board[i][j] = temp
                return result
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(word,i,j):
                    return True
        return False
