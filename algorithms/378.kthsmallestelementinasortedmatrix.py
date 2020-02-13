# 378. Kth Smallest Element in a Sorted Matrix leet code
#referenced from https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/505720/Python3-heap-solution
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix[0])
        heap= []
        for i in range(n):
            heapq.heappush(heap, (matrix[0][i],0, i))  # push some data in to get started with heap
        for i in range(k):
            val, row, col = heapq.heappop(heap)   # pop the smallest value
            if row+1<n:
                heapq.heappush(heap,(matrix[row+1][col], row+1, col))  # insert new value from row below. because current row is already in
        return val
