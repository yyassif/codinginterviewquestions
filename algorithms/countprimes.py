#sieve of eratosthenes 
#count the number of prime numbers less than n
import math
class Solution(object):
    def countPrimes(self, n):
        arr = [0]*(n) #number less than n
        i=2
        while i*i<=n:
            if arr[i]==1:
                continue
            for j in range(i*i,n,i):
                arr[j]=1
            i+=1
        cnt=0
        for i in range(2,n):
            if arr[i]==0:
                cnt+=1
        return cnt
        
#naive solutin - too slow
# class Solution(object):
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         cnt=0
#         def isPrime(num):
#             for i in range(2,num//2+1):
#                 if num%i==0:
#                     return False
#             return True
#         for i in range(2,n):
#             if isPrime(i):
#                 cnt+=1
#         return cnt
