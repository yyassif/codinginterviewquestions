class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        dic={}
        maxi=1
        numset = set(nums)
        for num in numset:
            temp = num
            cnt=1
            if num-1 not in numset:
                while temp+1 in numset:
                    temp = temp+1
                    cnt+=1
                    maxi = max(cnt, maxi)
        return maxi
