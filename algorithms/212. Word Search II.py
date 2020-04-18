#https://leetcode.com/problems/word-search-ii/discuss/499680/Python-3-Trie-and-dfs-beats-93-memory
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def inBounds(i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[i])
        
        def dfs(i, j, trie, path):
            
            letter = board[i][j]
            
            if letter not in trie:
                return
            
            path.append(letter)
            trie = trie[letter]
            
            if "$" in trie:
                self.result.add("".join(path))
            
            for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                di = i + dx
                dj = j + dy
                
                if inBounds(di, dj) and (di, dj) not in self.visited:
                    self.visited.add((di, dj))
                    dfs(di, dj, trie, path[:])
                    self.visited.remove((di, dj))
        
        self.visited = set()
        self.result = set()
        trie = self.buildTrie(words)
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.visited.add((i, j))
                dfs(i, j, trie, [])
                self.visited.remove((i, j))

        return self.result
        
    def buildTrie(self, words):
        
        trie = {}
        head = trie
        
        for word in words:
            for letter in word:
                if letter not in trie:
                    trie[letter] = {}
                trie = trie[letter]
            trie['$'] = {}
            trie = head
        return trie
