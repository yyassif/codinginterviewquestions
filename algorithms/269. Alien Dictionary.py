# https://leetcode.com/problems/alien-dictionary/discuss/581952/94-faster-Kahn's-Algo
#BFS topological sorting / Kahn's algo
class Solution:
    def alienOrder(self,words):
        chars = {c for x in words for c in x }
        
        graph = defaultdict(list)
        i_degree = defaultdict(int)

        for word1, word2 in zip(words, words[1:]):
            for char1, char2 in zip(word1, word2): #compare letter by letter for each words
                if char1 != char2:
                    graph[char1].append(char2)
                    i_degree[char2] += 1
                    break
            else:
                if len(word1) > len(word2): return ""

        Q = [x for x in chars if i_degree[x] == 0]
        L = []  #return array

        while Q:
            n = Q.pop(0) #BFS here but work either way BFS/DFS
            L.append(n)    #add to return list since in_degree==0

            for node in graph[n]:
                i_degree[node] -= 1
                if i_degree[node] == 0:
                    Q.append(node)

        return "".join(L) if len(L) == len(chars) else ""
