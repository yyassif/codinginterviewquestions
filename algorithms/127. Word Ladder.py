#solve using BFS and preprocessing
#runtime and space- O(M*N)
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L = len(beginWord)
        if L==0 or not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        dic = defaultdict(set)
        for word in wordList:
            for i in range(L):
                pat = word[:i]+"*"+word[i+1:]
                dic[pat].add(word)
        # print(dic)
        
        visited={beginWord:True}
        q=[]
        q.append((beginWord,1))
        min_step = float('inf')
        while q:
            word,step = q.pop(0)
            print(word, step)
            visited[word]=True
            if word==endWord:
                min_step=min(min_step, step)
                continue
            for i in range(L):
                pat = word[:i]+"*"+word[i+1:]
                for adj in dic[pat]:
                    if adj not in visited:
                        q.append((adj, step+1))
        return 0 if min_step==float('inf') else min_step
                        
            
        
