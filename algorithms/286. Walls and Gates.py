#286. Walls and Gates.py
#my own sol using bfs
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        nr=len(rooms)
        if rooms is None or nr==0:
            return rooms
        nc = len(rooms[0])
        if nc==0:
            return rooms
        INF = 2**31-1
        def valid(a,b,visited):
            if 0<=a<nr and 0<=b<nc and 0<rooms[a][b]<=INF and (a,b) not in visited:
                return True
            return False
        def bfs(a,b):
            visited = set()
            q=[]
            q.append((a,b,0))
            visited.add((a,b))
            while q:
                i,j,step = q.pop(0)
                # print(i,j,step)
                visited.add((i,j))
                if rooms[i][j] > step:
                    rooms[i][j] = step
                if valid(i,j-1,visited):
                    q.append((i,j-1,step+1))
                if valid(i,j+1,visited):
                    q.append((i,j+1,step+1))
                if valid(i-1,j,visited):
                    q.append((i-1,j,step+1))
                if valid(i+1,j,visited):
                    q.append((i+1,j,step+1))
            del visited
        #find gates 
        gates=[]
        for i in range(nr):
            for j in range(nc):
                if rooms[i][j]==0:
                    gates.append((i,j))
        
        for gate in gates:
            bfs(gate[0],gate[1])
        return rooms
                
