#k frequent element = print top k number of most frequent elements
from operator import itemgetter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        size = len(nums)
        if size==1:
            return [nums[0]]
        map = {}
        for n in nums:
            try:
                map[n]+=1
            except:
                map[n] = 1
        # freqmap = {}
        # for key,v in map.items():
        #     try:
        #         freqmap[v].append(key)
        #     except:
        #         freqmap[v] = []
        #         freqmap[v].append(key)
        map = sorted(map.items(),key=lambda v:v[1], reverse=True)
        print(map)
        kfrequent = []
        for i in range(k):
            kfrequent.append(map[i][0])
        return kfrequent
