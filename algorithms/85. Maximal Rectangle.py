class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            #pre-calculate row of heights
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1] #stores index i
            for i in range(n + 1):
                #find the max width
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w) #update max rectangle
                stack.append(i)
        return ans
