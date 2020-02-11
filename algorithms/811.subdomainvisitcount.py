# 811.subdomainvisitcount.py
# Myungho Sim
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        map = {}
        def get_subdomains(string):
            splits = string.split()
            subdomains = []
            size = len(splits)
            for i in reversed(range(size)):
                temp =""
                for j in range(i,size-1):
                    temp+= splits[j] +"."
                temp += splits[size-1]
                subdomains.append(temp)
            return subdomains
        
        for domain in cpdomains:
            cnt, full = domain.split()
            full = full.replace("."," ")
            subdomains = get_subdomains(full)
            for level in subdomains:
                if level in map:
                    map[level] = map[level] + int(cnt)
                else:
                    map[level]=int(cnt)
        ret = []
        for key in map:
            temp = str(map[key]) + " " + key
            ret.append(temp)
        return ret
        
        
