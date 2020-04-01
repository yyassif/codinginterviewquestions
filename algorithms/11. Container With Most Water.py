class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi_area=0
        l=0
        r=len(height)-1
        while l<r:
            maxi_area = max(maxi_area, abs(l-r)*min(height[l],height[r]))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxi_area
