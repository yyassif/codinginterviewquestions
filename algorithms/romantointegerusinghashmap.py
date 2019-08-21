#Myungho Sim
#roman to integer using hashmap. ideas taken from leetcode discussions.
class Solution:
    def romanToInt(self, s: str) -> int:
        map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        prev=0
        val=0
        for c in reversed(s):
            if prev<=map[c]: #VI, III
                val+=map[c]
                prev = map[c]
            else:
                val-=map[c]
        return val
                
