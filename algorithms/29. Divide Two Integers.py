#use dictionary and deal with irrational numbers for repeating decimals
#sol https://leetcode.com/articles/divide-integers/
#Approach 2: Repeated Exponential Searches  runtime complexity-O(log(n)*log(n)), space(1)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2**31-1
        MIN = -2**31
        HALF_MIN = MIN//2
        if dividend == MIN and divisor==-1:
            return MAX
        num_neg=0
        if dividend<0:
            num_neg+=1
            dividend *=-1
        if divisor<0:
            num_neg+=1
            divisor*=-1
        q=0 #quotient
        while divisor<=dividend:
            power = 1 #powers of two
            value = divisor
            while value<=-HALF_MIN and value+value<=dividend:
                value+=value
                power+=power
            q+=power
            dividend-=value
        return q if num_neg!=1 else -q
                
