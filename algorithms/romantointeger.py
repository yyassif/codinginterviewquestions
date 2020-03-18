# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {"I":1, "V":5, "X":10,"L":50,"C":100,"D":500,"M":1000, "S":10000}
        pre="S" #start
        stack=[]
        for digit in s:
            if sym[digit]<=sym[pre]:
                stack.append(int(sym[digit]))
            elif sym[digit]>sym[pre]:
                stack.pop()
                stack.append(int(sym[digit]-int(sym[pre])))
            pre = digit
        return sum(stack)
