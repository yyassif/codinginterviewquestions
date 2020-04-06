# video explanation https://www.youtube.com/watch?v=CsGP_s_3GWg
# https://www.youtube.com/watch?v=CsGP_s_3GWg
# algo explnation : https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
# tutorial https://www.youtube.com/watch?v=aZXi1unBdJA&list=PLQealZQ7ajwjIQUoHHnz17KNG-tixkw6P&index=3
# https://www.youtube.com/watch?v=2kREIkF9UAs
class Solution:
    import collections
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dic = collections.defaultdict(set)
        for u,v in connections:
            dic[u].add(v)
            dic[v].add(u)
        steps = [-1]*n
        res=[]
        self.dfs(0,-1,0,steps,dic,res)
        return res
        
    def dfs(self, cur, par, level, steps, dic,res): #par=parent
        steps[cur] = level
        
        for child in dic[cur]: #dic contains all the vertices #child== "to", cur="at"
            if child == par: #skip parent
                continue
            if steps[child] == -1: #if "to" is unvisited
                min_step = self.dfs(child, cur, level+1, steps, dic, res)
                steps[cur] = min( steps[cur], min_step) #propagate minimum edge/step down to its children
            else: #if "to" vertex is visited
                steps[cur] = min(steps[cur],steps[child])  #if it points back to child==parent, it will update w/ parent's min step value
        if steps[cur] == level and cur !=0: #articulation point. not root. its step equals level
            res.append([cur,par])
        return steps[cur]
