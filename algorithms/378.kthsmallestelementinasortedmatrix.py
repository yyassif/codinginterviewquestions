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

#brute force using heap would be O(log(n^2) since you put all the itmes in and use heap to get k items. 
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        if n==0:
            return -1
        arr=[]
        heapq.heapify(arr)
        for i in range(n):
            for j in range(n):
                if len(arr)<k:
                    heapq.heappush(arr, -matrix[i][j])
                else:
                    if matrix[i][j]<=-arr[0]: #front of the heap is max since multiplied by -1
                        heapq.heappop(arr)
                        heapq.heappush(arr, -matrix[i][j])
                # print(arr,matrix[i][j],arr[-1])
        return -heapq.heappop(arr)
