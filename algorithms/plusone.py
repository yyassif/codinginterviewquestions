#Myungho Sim
#plus one problem at leetcode
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry=1 #start at 1. because we are adding one at start
        sum =0
        for d in digits[::-1]: #reverse digits to start from one's digit
            sum = (d+carry)%10
            res.append(sum)
            carry = (d+carry) // 10
        if carry==1:
            res.append(carry)
        return res[::-1]
