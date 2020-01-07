class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #solution1 by merging and sorting
        for i in range(n):
            nums1.pop()
        for num in nums2:
            nums1.append(num)
        nums1.sort()
