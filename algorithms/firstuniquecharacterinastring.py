#Myungho Sim
#First unique character in a string
#solved using hashmap
class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for c in s:
            try:
                val = map[c]
                map[c] = val+1
            except:
                map[c]=1
        for i in range(len(s)):
            if(map[s[i]]==1):
                return i
        return -1
