#41.firstmissingpositive.py
#reference https://leetcode.com/articles/first-missing-positive/
#cycle sort
Another O(n) solution use cycle sort:
#****If number is not missing, nums array should hav numbers between 1~N. if that's the case, return the next number N+1
def firstMissingPositive(self, nums: List[int]) -> int:
    i = 0
    n = len(nums)
    while i < n:
        j = nums[i] - 1
        # put num[i] to the correct place if nums[i] in the range [1, n]
        if 0 <= j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    # so far, all the integers that could find their own correct place 
    # have been put to the correct place, next thing is to find out the
    # place that occupied wrongly
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

#leet code sol
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)  #size of nums array
        
        # Base case.
        if 1 not in nums:
            return 1
        
        # nums = [1]
        if n == 1:   # size 1 array must have 1 since negative and num>size will be replaced
            return 2
        
        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain 
        # only positive numbers.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # multiply by one to record idx of missing numbers, NOT THE NUMBER ITSELF
        # ****index of missing number DO NOT CORRESPOND with nums[idx] *********
        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array. 
        # If nums[2] is positive - number 2 is missing.
        for i in range(n): 
            temp = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if temp == n:     #encode the number n at index 0 since there are no zeroes. 
                nums[0] = - abs(nums[0])
            else:      #if number is not n then encode the number with a negative sign at index==number in nums array
                nums[temp] = - abs(nums[temp])
            
        # Now the index of the first positive number 
        # is equal to first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i   #missing # is encoded as positve INDEX val==missing num
        
        if nums[0] > 0: # value N is missing in nums since nums[0] is positive
            return n
            
        return n + 1     #no numbers are missing. return the next num in sequence.
