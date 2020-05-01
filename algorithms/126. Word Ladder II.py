#more good sol https://leetcode.com/problems/word-ladder-ii/discuss/490116/Three-Python-solution%3A-Only-BFS-BFS%2BDFS-biBFS%2B-DFS
import collections
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        dic = collections.defaultdict(set)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                pat = word[:i]+'*'+word[i+1:]
                dic[pat].add(word)
        visited={} #store distances
        visited[beginWord]=1
        prev_dic = {}
        q=[]
        q.append((beginWord, [], 1)) #word, path, dist
        ret = []
        shortest= float('inf')
        while q:
            word, path, dist =q.pop(0)
            print(word)
            if dist>shortest:
                break
            for i in range(L):
                pat = word[:i]+'*'+word[i+1:]
                for adj in dic[pat]:
                    if adj==word:
                        continue
                    if adj==endWord:
                        ret.append(path+[word]+[endWord])
                        shortest=dist
                        continue
                    if adj not in visited or visited[adj]>=dist: #found shorter step
                        q.append((adj, path+[word],dist+1))
                        visited[adj]= dist
        return ret
