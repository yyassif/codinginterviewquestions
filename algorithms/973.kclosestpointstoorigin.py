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
