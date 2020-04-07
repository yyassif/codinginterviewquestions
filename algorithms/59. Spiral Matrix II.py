# OOOO
# OOOO
# OOOO
# OOOO

# Top 
# XXX
# Right
# X
# X
# X
# Bottom
# XXX
# Left 
# X
# X
# X
# finish with  T ->R->B->L for one each side for the inner 2x2

#my own sol
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m=[[0 for _ in range(n)] for _ in range(n)]
        side=n-1
        r=0
        c=n-1
        cnt=1
        loop=0
        while (side>=1 and n%2==0) or (side>1 and n%2==1):
            for i in range(loop,side):
                m[r][i] = cnt
                cnt+=1
            for i in range(loop,side):
                m[i][c] = cnt
                cnt+=1
            for i in range(loop,side):
                m[n-r-1][n-i-1] = cnt
                cnt+=1
            for i in range(loop,side):
                m[n-i-1][n-c-1]=cnt
                cnt+=1
            side-=1
            r+=1
            c-=1
            loop+=1
        if n%2==1:
            m[n//2][n//2]=cnt
        return m
    

#similar sol from discussions

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        cnt=1
        m=[[0 for _ in range(n)] for _ in range(n)]
        a=0
        b=n-1
        while a<b:
            #Top
            for i in range(a,b):
                m[a][i]=cnt
                cnt+=1
            for i in range(a,b):
                m[i][b]=cnt
                cnt+=1
            for i in range(b,a,-1):
                m[b][i]=cnt
                cnt+=1
            for i in range(b,a,-1):
                m[i][a]=cnt
                cnt+=1
            a+=1
            b-=1
        if n%2==1:
            m[a][b]=cnt #or replace both a and b with n//2
        return m
        
