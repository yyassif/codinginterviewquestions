#973. K Closest Points to Origin

#divide and conquer- quickselect algo O(n)
class Solution(object):
    def kClosest(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return
            mid = partition(i, j)  
            if K < mid - i + 1:  #e.g. N=25, first bucket=10, 2nd=15, K=5, then only sort the first bucket
                sort(i, mid - 1, K) #only need to sort the first K in the first bucket(left of mid poviot)
            elif K > mid - i + 1:
                # K greater than pivot, find the remainder of K (K-size of 1st bucket) in the 2nd bucket 
                sort(mid + 1, j, K - (mid - i + 1))  

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]
#solution using heapq
# O(nlogk) time and O(k) space, because there are K elements in the heap.
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        arr = []
        for point in points:
            dist = point[0]**2+point[1]**2
            arr.append((dist, point))
        heapq.heapify(arr)
        ret = []
        for i in range(K):
            ret.append(heapq.heappop(arr)[1])
        return ret
    
#use sort O(nlogn)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        arr = []
        for idx,point in enumerate(points):
            print("point:",point)
            x,y = point
            arr.append((x**2+y**2, idx))
        arr.sort()
        ret = [points[tuple[1]] for tuple in arr[:K]]
        return ret
