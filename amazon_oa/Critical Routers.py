#Critical Routers
#https://leetcode.com/discuss/interview-question/436073/
Python solution, the same idea in 1192. Critical Connections in a Network.

Time complexity: O(n)
Space complexity: O(n)
import collections

class Solution(object):
    def critical_routers(self, numNodes, numEdges, edges):
        """
        :type numNodes: int
        :type numEdges: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        self.value_graph = collections.defaultdict(list)
        value_list = [-1] * numNodes
        self.res = []

        for i in range(numEdges):
            a, b = edges[i]
            self.value_graph[a].append(b)
            self.value_graph[b].append(a) 

        self.dfs(-1, 0, 0, value_list)

        return self.res

    def dfs(self, a, b, count, value_list):
        value_list[b] = count + 1
        
        for node in self.value_graph[b]:
            if node == a:
                continue
            elif value_list[node] == -1:
                temp_value = self.dfs(b, node, count + 1, value_list)
                value_list[b] = min(value_list[b], temp_value)
            else:
                value_list[b] = min(value_list[b], value_list[node])
                
        if value_list[b] == count + 1 and b != 0:
            self.res.append(a)
                
        return value_list[b]


def main():
    numNodes = 7
    numEdges = 7
    edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
    solution = Solution()
    res = solution.critical_routers(numNodes, numEdges, edges)
    print(res)

if __name__ == "__main__": 
    main()
