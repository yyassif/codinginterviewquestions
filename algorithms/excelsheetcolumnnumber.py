#Myungho Sim
#Excel sheet column number on leetcode
#better than 95% of submissions
class Solution:
    def titleToNumber(self, s: str) -> int:
        output = 0
        size = len(s)
        for i in range (size):
            asc = ord(s[i])
            num = asc-64
            output =output*26+num
        return output
            
