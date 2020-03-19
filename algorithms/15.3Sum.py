#two pointer sol https://leetcode.com/problems/3sum/discuss/534179/Python-O(n2)-sol.-by-two-pointers.-80%2B-w-Hint
class Solution: 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        solution = []
        for idx in range(0, size-2):
			# avoid repetition
            if idx and nums[idx] == nums[idx-1]:
                idx +=1
                pass
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
