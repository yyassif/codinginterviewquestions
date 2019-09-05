#Myungho Sim
#number of 1 bits problem @ leetcode
#faster than 98% submissions
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt=0
        while n!=0:
            if n&1==1:
                cnt+=1
            n=n>>1    
        return cnt
