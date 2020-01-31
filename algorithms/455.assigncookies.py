# Myungho Sim
# 455 assign cookies
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cnt = 0
        g.sort()
        s.sort()
        g_idx=0
        s_idx=0
        while g_idx<len(g) and s_idx<len(s):
            if g[g_idx]<= s[s_idx]:
                cnt+=1
                g_idx+=1
                s_idx+=1
            else:
                s_idx+=1
        return cnt
