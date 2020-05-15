class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            #add to stack if heights increase and keep popping as smaller heights found
            while(stack and heights[stack[-1]] > heights[i]):
                h = heights[stack.pop()]
                w = i-stack[-1]-1
                ans = max(ans, w*h)  #keep updating max area
            stack.append(i) #keep adding index if heights increase
        return ans
