# 139. Word Break from leetcode
#memoization, recursion - passes all tests
class Solution(object):
    def __init__(self):
        self.d = {}     # without proper init of global vars some tests are failing - a known leetcode issue
    def wordBreak(self, s, wordDict): 
        if not s: return False
        if s in wordDict: return True
        for w in wordDict:
            if w==s[:len(w)]:
                if s[len(w):] not in self.d:
                    self.d[s[len(w):]] = self.wordBreak(s[len(w):], wordDict)
                    if  self.d[s[len(w):]]:   return True
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
