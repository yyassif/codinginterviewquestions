#load balancer Amazon OA question
from typing import List

def balancing_possible(nums: List[int]) -> bool:
    if len(nums) < 5:
        return False
        
    total_sum = sum(nums)
    left_index, right_index = 1, len(nums) - 2
    left_sum, right_sum = nums[0], nums[-1]
    
    while left_index < right_index:
        drop_sum = nums[left_index] + nums[right_index]
        mid_sum = total_sum - drop_sum - left_sum - right_sum
        
        if mid_sum < left_sum or mid_sum < right_sum:
            return False
        if left_sum == mid_sum == right_sum:
            return True
        
        if left_sum <= right_sum:
            left_sum += nums[left_index]
            left_index += 1
        else:
            right_sum += nums[right_index]
            right_index -= 1
    
    return False

print(balancing_possible([1, 3, 4, 2, 2, 2, 1, 1, 2])) # true
print(balancing_possible([1, 1, 1, 1, 1, 1])) # false
print(balancing_possible([1, 2] * 10000)) # true
