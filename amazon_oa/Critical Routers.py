#Critical Routers
#https://leetcode.com/discuss/interview-question/436073/
Python solution, the same idea in 1192. Critical Connections in a Network.

Time complexity: O(n)
Space complexity: O(n)

import collections
class Solution(object):
	def critical_routers(self, numNodes, numEdges, edges):
		self.dic = collections.defaultdict(set)
		for u,v in edges:
			self.dic[u].add(v)
			self.dic[v].add(u)
		levels=[-1]*numNodes
		self.ret=[]
		self.dfs(0,-1,0, levels) #start at "root", par =-1, level=0
		return self.ret
	def dfs(self, cur, par, level, levels):
		levels[cur] = level+1
		for adj in self.dic[cur]:
			if adj==par: #skip parent
				continue
			if levels[adj]==-1: #check if "to" is unvisited
				min_step = self.dfs(adj, cur, level+1, levels)
				levels[cur] =  min(min_step, levels[cur])  #propagate minimum edge/step down to its children
			else: #if "to" vertex is visited
				levels[cur] = min(levels[cur], levels[adj])
		if levels[cur]==level+1 and cur!=0: #articulation point. not root. its step equals level
			self.ret.append(par)
		return levels[cur]


def main():
    numNodes = 7
    numEdges = 7
    edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
    solution = Solution()
    res = solution.critical_routers(numNodes, numEdges, edges)
    print(res)

if __name__ == "__main__": 
    main()
