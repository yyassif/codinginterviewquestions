#leetcode sol
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {}) #set {} as default value for this key
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False) #set False as default value if WORD_KEY does not exist
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords    
##########################################################################################
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
