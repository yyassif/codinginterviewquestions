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

#less efficient sliding window sol
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n= len(s)
        s=s.replace(" ","#")
        if n==0:
            return 0
        i=0
        j=0
        ans=0
        map ={}
        while i<n and j<n:  #sliding window
            #when s[i] is removed, this section runs again. e.g. abcabcbb
            if s[j] not in map:  #e.g. abc and then remove a and then this segment runs again with a. a mapped. j=4 and i=1
                map[s[j]] = 1
                j+=1
                ans = max(ans, j-i)
            else:
                del map[s[i]] #removes s[i] which is left end and s[j]=right end is checked again
                i+=1
            print(i,j,ans)
        return ans
            

  
