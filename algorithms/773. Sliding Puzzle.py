class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        b_str= ''.join([str(c) for c in board[0]+board[1]]) #flatten 2d board in 1d strings
        start = b_str.index('0')
        stack = [[start,b_str, 0]]  #start idx, steps
        #hard code neighbors since it's only 2x3 board
        neighbors = {0:(1,3),1:(0,2,4),2:(1,5),3:(0,4),4:(1,3,5),5:(2,4)} #2d to 1d flattened directions
        visited=set()
        while stack:
            idx, string, step = stack.pop(0)
            if string=='123450':
                return step
            elif string in visited:
                continue
            else:
                visited.add(string)
                for neighbor in neighbors[idx]: #directions
                    temp = list(string) #board string representation to list of strings
                    temp[idx],temp[neighbor] = temp[neighbor],temp[idx] #slide or swap tiles
                    temp_string = ''.join(temp)
                    stack.append((neighbor, temp_string, step+1))
        return -1
