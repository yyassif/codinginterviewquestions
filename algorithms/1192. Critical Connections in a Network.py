# video explanation https://www.youtube.com/watch?v=CsGP_s_3GWg
# https://www.youtube.com/watch?v=CsGP_s_3GWg
# algo explnation : https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
class Solution:
    import collections
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dic = collections.defaultdict(set)
        for u,v in connections:
            dic[u].add(v)
            dic[v].add(u)
        steps = [-1]*n
        res=[]
        self.helper(0,-1,0,steps,dic,res)
        return res
        
    def helper(self, cur, par, level, steps, dic,res):
        steps[cur] = level
        
        for child in dic[cur]:
            if child == par:
                continue
            if steps[child] == -1:
                min_step = self.helper(child, cur, level+1, steps, dic, res)
                steps[cur] = min( steps[cur], min_step)
            else:
                steps[cur] = min(steps[child],steps[cur])
        if steps[cur] == level and cur !=0:
            res.append([cur,par])
        return steps[cur]
