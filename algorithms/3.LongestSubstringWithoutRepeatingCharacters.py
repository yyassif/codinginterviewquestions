# 3. Longest Substring Without Repeating Characters
#optimized solution 2 based on sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0 or n==1:
            return n
        map={}
        i=0
        j=0
        maxsize=0
        while j<n:
            if map.get(s[j])!=None:
                i = max(i, map.get(s[j]))
            map[s[j]] = j+1
            maxsize = max(maxsize,j-i+1)
            j+=1
        return maxsize

# sol 1 based on leetcode solution in java - sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0 or n==1:
            return n
        map={}
        i=0
        j=0
        maxsize=0
        while i<n and j<n:
            if map.get(s[j])==None:
                map[s[j]] = j
                j+=1
                maxsize = max(maxsize, j-i)
            else:
                del map[s[i]]
                i+=1 #i is updated whenever duplicates are detected.
            
        return maxsize

  
