# 139. Word Break from leetcode
#memoization, recursion - passes all tests
class Solution(object):
    def __init__(self):
        self.d = {}     # without proper init of global vars some tests are failing - a known leetcode issue
    def wordBreak(self, s, wordDict): 
        if not s: return False
        if s in wordDict: return True
        for w in wordDict: 
            if w==s[:len(w)]:  #check the front part of string s if any words in wordDict matches
                if s[len(w):] not in self.d: #check the remainder of substring s
                    self.d[s[len(w):]] = self.wordBreak(s[len(w):], wordDict)
                    if  self.d[s[len(w):]]:   return True
        return False	

#########################################################################    
#BFS method
from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
		s = "catsandog"
		wordDict = ["cats", "dog", "sand", "and", "cat"]
        0 1 2 3 4 5 6 7 8 9
        c a t s a n d d o g
		queue = [0]
		you find 'cat' and 'cats'
		queue = [3,4]
		you find 'and‘  and 'sand'
		queue = [7]
		you find 'dog', which you reached the end.
         0
        / \
      cat  cats
      /      \
    sand     and
    /         \
    dog       dog
        """
        visited = set()
        queue = deque([0])
        while queue:
            start = queue.popleft()
            if start not in visited:
                for end in range(start + 1, len(s)+1):
                    if s[start:end] in wordDict:
                        queue.append(end)
                        if end == len(s):
                            return True
                visited.add(start)
        return False


#########################################################################
#brute force solution - passes some cases,time limit exceeded
s = "cars"
wordDict = ["car","ca","rs"]
size = len(s)
start=0
found = False
def rec(start):
    if start==size:
        return True
    end = start+1
    for end in range(start, size+1):
        print(start,end)
        if s[start:end] in wordDict and rec(end):
            return True
    return False
print(rec(0))
