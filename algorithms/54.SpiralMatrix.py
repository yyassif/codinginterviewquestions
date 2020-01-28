#Myungho Sim
#54. Spiral Matrix  
#better than 63% runtime, 100% memory
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rmin = 0
        rmax = len(matrix)-1 #num rows
        if rmax==-1:
            return
        cmin = 0
        cmax = len(matrix[0])-1 # num columns
        if cmax==-1:
            return
        ret = []
        maxsize = len(matrix)*len(matrix[0])
        cnt=0
        dir="r"
        r=0
        c=0
        for i in range(maxsize):
            print(ret)
            print(r,c)
            ret.append(matrix[r][c])
            if dir=="r": 
                if c==cmax:
                    dir="d"
                else:
                    c+=1
                                                    
            if dir=="d":
                if r==rmax:
                    dir="l"
                else:
                    r+=1
            if dir=="l":
                if c==cmin:
                    dir="u"
                else:
                    c-=1
            if dir=="u":
                if r==rmin+1:
                    dir="r"
                    cmin+=1
                    cmax-=1
                    rmin+=1
                    rmax-=1
                    c+=1
                else:
                    r-=1
                    
        return ret
