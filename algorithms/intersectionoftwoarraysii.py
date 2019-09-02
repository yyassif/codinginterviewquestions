#Myungho Sim
#intersection of two arrays - linear solution using hash map
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1={}
        res = []
        #map longer set.
        #make sure nums1 is longer. otherwise swap
        if len(nums1)<len(nums2):
            t = nums2
            nums2 = nums1
            nums1 = t
        #build hash map of larger num list
        for n in nums1:
            try:
                val = map1[n]
                map1[n] = val+1
            except:
                map1[n] =1
        #search through hash map. decrement count as you visit.
        for n in nums2:
            try:
                val = map1[n]
                if(val>=1):
                    val-=1
                    map1[n] = val
                    res.append(n)
            except:
                pass
        return res
        
