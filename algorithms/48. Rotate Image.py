#sol from leet code Approach 1 : Transpose and then reverse
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            #important!! it will reverse back to original if j has range(0,n)
            for j in range(i,n): #skip first i col since already swapped.
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
        for i in range(n):
            matrix[i].reverse()
#sol 2          
class Solution:
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range(n // 2 + n % 2): #up to the middle half. if odd, add n%2
            for j in range(n // 2): #up to the middle
                tmp = [0] * 4
                row, col = i, j
                # store 4 elements in tmp
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    print("B:",row, col)
                    row, col = col, n - 1 - row #gives you the seq 0,0->0,2->2,2,-> 2,0 when n=3
                    print("A:",row, col)
                # rotate 4 elements   
                for k in range(4):
                    matrix[row][col] = tmp[(k - 1) % 4] #rotate temp arr @k=0:-1->3, k=1->0, k=2->1,k=3->2
                    row, col = col, n - 1 - row
#sol3 pass through matrix once
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])        
        # rotate the four corners. iterate through the matrix by shifting
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                #swap with opposite corners
                tmp = matrix[n - 1 - j][i]  #store copy of of the first cell
                #IMPORTANT [J..**][i]  =           [I***][J....*]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]   #working backwards, 2,0=2,2
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]    #2,2=0,2
                matrix[j][n - 1 - i] = matrix[i][j]                   #0,2=0,0
                matrix[i][j] = tmp                                    #0,0 = tmp(2,0)
