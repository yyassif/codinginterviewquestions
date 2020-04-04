#973. K Closest Points to Origin
#solution using heapq
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
#divide and conquer- O(n)

    
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
