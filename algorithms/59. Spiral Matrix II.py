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
        
