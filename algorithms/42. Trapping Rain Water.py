#stack sol time-O(n) ,space O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack =[]
        area = 0
        
        for i in range(len(height)):
            offset = 0
            while(stack and height[i] >= height[stack[-1]]):
                pre_i = stack.pop()
                area += (height[pre_i]-offset) * (i-pre_i-1)   #idx needs to be at least one apart. e.g. [2,0,2]
                offset = height[pre_i]
            if stack:
                area += (height[i]-offset) * (i-stack[-1]-1)
            stack.append(i)
            
        return area
    
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
            
                    
            
