#Myungho Sim
#leetcode - implement strstr
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size_h = len(haystack)
        size_n = len(needle)
        if(size_h==0 and size_n ==0):
            return 0
        elif(size_h==size_n and haystack==needle):
            return 0
        for i in range(size_h-size_n+1):
            mismatch = False
            for j in range(size_n):
                if haystack[i+j]!=needle[j]:
                    mismatch = True
                    break
            if(mismatch == False):
                return i
        return -1
