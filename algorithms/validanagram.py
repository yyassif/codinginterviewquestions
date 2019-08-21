#Myungho Sim
#valid anagram problem @ leetcode
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        size_s = len(s)
        size_t = len(t)
        if size_s!=size_t:
            return False
        val=0
        for i in range(size_s):
            try:
                val = map[s[i]]
                map[s[i]] = val+1
            except:
                map[s[i]] = 1
        print(map)
        for i in range(size_t):
            try:
                val = map[t[i]]
                map[t[i]] = val-1
            except:
                return False
        print(map)
        for k,v in map.items():
            if v!=0:
                return False
        return True
                
