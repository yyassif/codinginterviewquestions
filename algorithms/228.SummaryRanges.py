# 228.SummaryRanges.py
#test cases 
# test #1 [0,1,2,4,5,7]
# test #2 [0,2,3,4,6,8,9]
# test #3 [2,4,6,8,10]
# my own solution
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(-1)
        n = len(nums)
        if n==0:
            return None
        i=0
        ret =[]
        def add_string(a,b):
            if a==b:
                ret.append(str(a))
            else:
                temp=str(a)+"->"+str(b)
                ret.append(temp)            
        while i+1<n:
            if nums[i]+1==nums[i+1]:
                end=i
                while end+1<n and nums[end]+1==nums[end+1]:
                    end+=1
                add_string(nums[i],nums[end])
                i=end+1
            else:
                add_string(nums[i],nums[i])
                i+=1
        return ret
