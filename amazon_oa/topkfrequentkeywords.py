# https://leetcode.com/discuss/interview-question/542597/
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

import re
from collections import Counter

class Element:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

def topKFrequent(k, keywords, reviews):
    '''
    k: int
    keywwords: list of string
    reviews: list of string
    '''
    word_list = []
    
    for review in reviews:
        word_list += set(review.lower().replace('[^a-z0-9]', '').split())
    
    count = Counter(word_list)
    
    heap = []
    
    for word, freq in count.items():
        if word in keywords:
            heapq.heappush(heap, Element(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
    
    return [heapq.heappop(heap).word for _ in range(k)][::-1]
    
print(topKFrequent(k, keywords, reviews))

#####################################################################################################
from re import sub
from collections import defaultdict
def top_K_freq_keywords(keywords, reviews, k):
	if not k or not keywords or not reviews: return []
	keys = set(keywords)
	word_count = defaultdict(int)
	for rev in reviews:
		words = rev.lower().split(" ")
		added = set()
		for word in words:
			word = sub("[^a-z]", "", word)
			if word in keys and word not in added:
				word_count[word] += 1
				added.add(word)
	result = sorted(word_count.keys(), key=lambda x: (-word_count[x], x))
	return result[:k]

keywords1 = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews1 = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

Following is the output:

>>> top_K_freq_keywords(keywords1, reviews1, 2)
['betacellular', 'anacell']
>>> top_K_freq_keywords(keywords, reviews, 2)
['anacell', 'betacellular']
Space Complexity: O(n)
RTC: O(n+k*logn)


k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]


Output:
["anacell", "betacellular"]

Explanation:
"anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
Example 2:

Input:
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

Output:
["betacellular", "anacell"]

Explanation:
"betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.
Related problems:

https://leetcode.com/problems/top-k-frequent-words/
https://leetcode.com/problems/top-k-frequent-elements/
#############################################################################################################
def topKFreqKeywords(reviews: List[str], keywords: List[str], k: int) -> List[str]:
    # clean review strings
    rs = [r.lower().translate(str.maketrans('','',string.punctuation)) for r in reviews]
    hashmap = dict.fromkeys(keywords, 0) # hashtable with keywords set to 0
    # can't figure out how to get around this double for loop
    for r in rs:
        for key in keywords:
            if key in r: hashmap[key] += 1
    return heapq.nlargest(k, hashmap.keys(), hashmap.get)
    
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]
keywords = ["anacell", "cetracular", "betacellular"]
k = 2

kay = 2
keywordss = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviewss = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
assert topKFreqKeywords(reviews,keywords,k) == ["anacell", "betacellular"]
assert topKFreqKeywords(reviewss,keywordss,kay) == ["betacellular", "anacell"]
#############################################################################################################
# sol 1
# space Complexity: O(n)
# RTC: O(n+k*logn)
def top(k, keywords, reviews):
    map = {}
    for key in keywords:
        for review in reviews:
            if key in review.lower():
                if key in map:
                    map[key]+=1
                else:
                    map[key] = 1
    ret = list(map)
    ret.sort(key = lambda x:(-map[x], x))
    return ret[:k]

k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
    "Anacell provides the best services in the city",
    "betacellular has awesome services",
    "Best services provided by anacell, everyone should use anacell",
]
ret = top(k, keywords, reviews)
print(ret)


k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
ret = top(k, keywords, reviews)
print(ret)

  
