class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        nr= len(image)
        nc = len(image[0])
        def valid(a,b,color):
            if 0<=a<nr and 0<=b<nc and image[a][b]==color:
                return True
            return False
        
        def bfs(a,b):
            directions = [(0,-1),(0,1),(1,0),(-1,0)]
            stack = []
            stack.append((a,b))
            color = image[a][b]
            if color==newColor:
                return
            while stack:
                x,y = stack.pop()
                if image[x][y]==color:
                    image[x][y] = newColor
                # elif image[x][y]==newColor:
                #     continue
                for direc in directions:
                    i = x+direc[0]
                    j = y+direc[1]
                    if valid(i,j,color):
                        stack.append((i,j))
        bfs(sr,sc)
        return image
        
