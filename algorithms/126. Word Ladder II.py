#more good sol https://leetcode.com/problems/word-ladder-ii/discuss/490116/Three-Python-solution%3A-Only-BFS-BFS%2BDFS-biBFS%2B-DFS
import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        search_que = collections.deque()
        visited = {}
        word_len = len(beginWord)
        visited[beginWord] = 1
        word_dict = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                new = word[:i] + "?" + word[i+1:]
                word_dict[new].add(word)
        prev_dic = {}
        break_flag = False
        search_que.append((beginWord, [], 1))
        rst = []
        shortest = None
        while search_que:
            word_tup = search_que.popleft()
            word, path, dist = word_tup
            if shortest and dist > shortest:
                break
            for ind in range(word_len):
                cur_word = word[:ind] + "?" + word[ind+1:]
                neighbors = word_dict[cur_word]
                for neighbor in neighbors:
                    if neighbor == word:
                        continue
                    tup = (neighbor, path + [word], dist + 1)
                    if neighbor == endWord:
                        rst.append(tup[1] + [endWord])
                        shortest = dist
                        continue
                    if neighbor not in visited or visited[neighbor] >= dist:
                        search_que.append(tup)
                        visited[neighbor] = dist
        return rst  
