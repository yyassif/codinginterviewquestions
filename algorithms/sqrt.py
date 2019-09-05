#Myungho Sim
#sqrt problem from leetcode
#ideas taken from leetcode discussion
#solution using binary search
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==1 or x==0:
            return x
        h=x
        l=0
        ret=0
        while l<=h:
            m=(l+h)//2
            if m*m==x:
                return m
            if m*m<x:
                l=m+1
                ret=m
            elif m*m>=x:
                h=m-1
        return ret
