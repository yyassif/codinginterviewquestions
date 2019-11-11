#faster than 98%, less space than 100% of submissions
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        inter=[]
        for n in nums1:
            map[n]=1
        for n in nums2:
            try:
                if map[n]==1:
                    map[n]=2
                    inter.append(n)
            except:
                pass
        return inter
            
