# 215. Kth Largest Element in an Array 
#sol adapted from https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/324338/Solution-Explained
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left=0
        right = len(nums)-1
        while left<=right:
            pivot_idx = random.randint(left, right)
            #must find pivot value here b/c pivot swapped with nums[right] @ partition method
            pivot = nums[pivot_idx] 
            new_idx = self.part(left, right,pivot_idx,pivot,nums)
            if new_idx==k-1:
                return nums[new_idx]
            elif new_idx>k-1:
                right = new_idx-1
            else:
                left = new_idx+1
        return -1
    def part(self,left, right, pivot_idx,pivot, nums):
            nums[pivot_idx],nums[right] = nums[right],nums[pivot_idx] #pivot swapped with nums[right]
            left_wr=left
            for i in range(left, right):
                if nums[i]>pivot:
                    nums[left_wr], nums[i] = nums[i],nums[left_wr]
                    left_wr+=1
            nums[left_wr], nums[right] =nums[right],nums[left_wr]
            return left_wr
