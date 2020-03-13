#using heapify
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)
        arr = [(-freq, w) for w, freq in counts.items()]
        heapq.heapify(arr)
        return [heapq.heappop(arr)[1] for _ in range(k)]

#shorter ver using collections.Counter and sort
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        items = list(count)
        items.sort(key=lambda x:(-count[x],x)) #(-count[x],x) for sorting alphabetically
        return items[:k]

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
