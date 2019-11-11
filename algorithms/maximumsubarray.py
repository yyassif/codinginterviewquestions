#solution2 greedy approach makes the most sense @ https://leetcode.com/articles/maximum-subarray/
#max sub array
#solution 1 dynamic programming approach
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_cum = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
            max_cum = max(nums[i], max_cum)
        return max_cum
                
        
#solution 2-naive solution. time out at leetcode
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_sum = [] #track cum_sum size 1,2,3,4
        cum =0
        max=-sys.maxsize-1
        for n in nums:
            if n>max:
                max=n
            cum+=n
            if cum>max:
                max=cum
            sub_sum.append(cum)
        size = len(nums)
        
        #check last two ~ last size-1 chunk
        for i in range(0, size-2):
            last_n_chunk = sub_sum[size-1]-sub_sum[i]
            if last_n_chunk>max:
                max=last_n_chunk
        #check middle of size 2 to size-2
        for mid_size in range(2,size-1):
            mid=0
            for i in range(0,size-mid_size-1):
                before=i
                #start = i+1
                end = i+mid_size
                mid =sub_sum[end]-sub_sum[before]
                if mid>max:
                    max=mid
        return max
                
