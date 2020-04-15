#two pointer sol https://leetcode.com/problems/3sum/discuss/534179/Python-O(n2)-sol.-by-two-pointers.-80%2B-w-Hint
#sol based on similar and easier problem
#related problem (easy) https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution: 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        solution = []
        for idx in range(0, size-2):
			# avoid repetition
            if idx and nums[idx] == nums[idx-1]: #idx is at least 1. e.g. avoid [[0,0,0]]
                idx +=1
                continue
            first_num = nums[idx]
            target = -first_num
            i, j = idx+1, size-1
            while i < j:
                cur_two_sum = nums[i] + nums[j]
                if cur_two_sum > target:
                    j -=1
                elif cur_two_sum < target:
                    i += 1
                else:
                    solution.append( [ first_num, nums[i], nums[j] ] )
                    i += 1
                    j -= 1
					# avoid repetition
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
					# avoid repetition
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
        return solution

