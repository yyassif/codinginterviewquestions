#         1.Why carry is a&b:
#         If a and b are both 1 at the same digit, it creates one carry.
#         Because you can only use 0 and 1 in binary, if you add 1+1 together, it will roll that over to the next digit, and the value will be 0 at this digit.
#         if they are both 0 or only one is 1, it doesn't need to carry.

#         Use ^ operation between a and b to find the different bit
#         In my understanding, using ^ operator is kind of adding a and b together (a+b) but ignore the digit that a and b are both 1,
#         because we already took care of this in step1.	


def getSum(self, a: int, b: int) -> int:
	carry = 0
    mask = 0xffffffff
    while b & mask != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    
    # for overflow condition like
    # -1
    #  1
    return a&mask if b > mask else a
	
	
#more explanation
https://leetcode.com/problems/sum-of-two-integers/discuss/167931/Solution-with-ACTUAL-explanation-(how-you-would-work-this-out)
