class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for i in range(9):
            check=[False]*9
            for j in range(9):
                if board[i][j].isdigit():
                    val= int(board[i][j])
                    if check[val-1]==False:
                        check[val-1]=True
                    else:
                        return False
        #check cols
        for i in range(9):
            check=[False]*9
            for j in range(9):
                if board[j][i].isdigit():
                    val= int(board[j][i])
                    if check[val-1]==False:
                        check[val-1]=True    
                    else:
                        return False
                
        #check 3x3 blocks
        for i in range(0,9,3):
            for j in range(0,9,3):
                check=[False]*9
                for k in range(3):
                    for l in range(3):
                        # print(i+k,j+l)
                        if board[i+k][j+l].isdigit():
                            val= int(board[i+k][j+l])
                            if check[val-1]==False:
                                check[val-1]=True
                            else:
                                return False
        return True
            
