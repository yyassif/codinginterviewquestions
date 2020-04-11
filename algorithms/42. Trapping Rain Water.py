#dynamic programming based on brute force sol
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==0:
            return 0
        left_max=[0]*n
        left_max[0] = height[0]
        right_max=[0]*n
        right_max[n-1] = height[n-1]
        for i in range(1,n):
            left_max[i]=max(left_max[i-1], height[i])
            
        for i in reversed(range(n-1)):
            right_max[i]=max(right_max[i+1], height[i])
        print("l", left_max)
        print("r", right_max)
        ret=0
        for i in range(1,n-1):
            ret+= min(left_max[i], right_max[i])-height[i]
            print(min(left_max[i], right_max[i]))
        return ret
        
###################################################################

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
            
                    
            
