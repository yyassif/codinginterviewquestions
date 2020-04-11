#brute force - time exceeded
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        arr = [0]*n
        if n<2:
            return 0
        for i in range(n):
            left_max=0
            if i==0:
                left_max=0
            else:
                for j in range(i):
                    left_max=max(left_max, height[j])
            right_max=0
            if i==n-1:
                right_max=0
            else:
                for j in range(i+1, n):
                    right_max = max(right_max, height[j])
            arr[i] = min(left_max, right_max)-height[i]
            if arr[i]<0:
                arr[i]=0
        return sum(arr)
            
                    
            
