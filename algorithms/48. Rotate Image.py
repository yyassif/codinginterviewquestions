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
                
