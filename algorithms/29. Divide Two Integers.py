#use dictionary and deal with irrational numbers for repeating decimals
#sol https://leetcode.com/articles/divide-integers/
#Approach 3: Adding Powers of Two
# Run- O(log(n)), space O(1)
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
        doubles=[]
        powers=[]
        #e.g. dividend 10000, divisor=30
        #doubles [30, 60, 120, 240, 480, 960, 1920, 3840, 7680]
        #powers [1, 2, 4, 8, 16, 32, 64, 128, 256]

        power=1
        while divisor<=dividend:
            doubles.append(divisor) #multiples of two of the divisor, e.g. 3, 6, 12, 24, 
            powers.append(power)   #same as the num of subtractions btw dividend and divisor
            if divisor>-HALF_MIN:
                break
            divisor+=divisor #double divisor
            power+=power
        for i in reversed(range(len(doubles))):
            if doubles[i] <=dividend:
                q+=powers[i]
                dividend-=doubles[i]
        return q if num_neg!=1 else -q
                

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
                
