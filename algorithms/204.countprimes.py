class Solution:
    def countPrimes(self, n: int) -> int:
        p=[True]*n
        cnt=0
        for i in range(2,n):
            if p[i]:
                cnt+=1
                j=2
                while i*j<n:
                    p[i*j]=False
                    j+=1
        return cnt
