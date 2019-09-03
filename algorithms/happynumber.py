#Myungho Sim
#happy number problem from leetcode
class Solution:
    def isHappy(self, n: int) -> bool:
        record = {}
        num = n
        while True:
            numStr = str(num)
            num=0
            for c in numStr:
                digit = int(c)
                num+=digit**2
            #check if it encountered same number before
            if num in record:
                return False
            #if num is one. return true. 
            if num==1:
                return True
            record[num] = True
        return False
