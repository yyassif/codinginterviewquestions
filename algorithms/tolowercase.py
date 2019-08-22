#Myungho Sim
#implement tolowercase in python @leetcode
class Solution:
    def toLowerCase(self, str: str) -> str:
        newstr=""
        num=0
        for c in str:
            num = ord(c)
            if num>=65 and num <=90:
                num+=32
            newc = chr(num)
            newstr+=newc
        return newstr
