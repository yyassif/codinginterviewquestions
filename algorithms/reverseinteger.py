#Myungho Sim
#leetcode : reverse an integer
class Solution:
    def reverse(self, x: int) -> int: 
        digit=0
        newNum=0
        isNegative = False
        if x<0:
            isNegative = True
            x = x*-1
        while x>0:
            digit = x %10
            newNum = newNum*10+digit
            x = int(x/10)
        #check for overflow of 32bit integer and return 0
        if newNum> 2**31-1:
            return 0
        if isNegative:
            newNum = -1*newNum
        return newNum
