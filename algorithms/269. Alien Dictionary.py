#https://leetcode.com/problems/alien-dictionary/discuss/390614/Python-BFS-Topological-Sorting
#BFS topological sorting / Kahn's algo
from typing import List
from collections import defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # calculate all edges (u->v, in which u must be ahead of v in alien dictionary)
        edges = defaultdict(set)
        degrees = defaultdict(int)
        for two_words in zip(words, words[1:]): # compare adjcent words
            for ch1, ch2 in zip(*two_words): # compare letter by letter between two words
                if ch1 != ch2: # ch1 -> ch2 (degree[ch2]++)
                    edges[ch1].add(ch2) # ch2 depends on (is after) ch1
                    break 
        # calculate in-degrees for all vertices
        for ch in edges.keys():
            for ch2 in edges[ch]:
                degrees[ch2] += 1
        
        charset = set(''.join(words)) # get all vertices
        q = [ch for ch in charset if ch not in degrees] # degree=0 as start nodes
        res = []
        while q:
            ch = q.pop(0)
            res.append(ch)
            for ch2 in edges[ch]:
                degrees[ch2] -= 1
                if degrees[ch2] == 0:
                    q.append(ch2)
        if all(map(lambda d: d==0, degrees.values())): # all vertex in degrees are zero, acyclic graphs
            return ''.join(res)
        return '' # otherwise, circle found in graph
