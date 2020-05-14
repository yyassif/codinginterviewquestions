#Myungho Sim

Approach #3 Bit Manipulation [Accepted]  run O(n) / O(1) space
#e.g. >>> (0^0)^(1^1)^(2^3)^3
2
missing number means from there should be numbers 0 to n+1 but with one missing
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

Approach #4 Gauss' Formula [Accepted] run O(n) / O(1) space
class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

#sol similar to hashset.  O(n) for both space and runtime
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        arr = [i for i in range(n+1)] #since one number is missing
        for num in arr:
            if num not in nums:
                return num

#hashset sol  O(n) for both space and runtime
class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

#missing number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        arr = [-1] * (size+1)
        for i in range(size):
            arr[nums[i]]=1
        try:
            num = arr.index(-1)
        except:
            num=-1
        return num
