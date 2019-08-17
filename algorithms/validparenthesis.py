#Myungho Sim
#leetcode problem : valid parenthesis
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        size = len(s)
        for i in range(size):
            digit = s[i]
            d = ""
            if digit=='(' or digit=='[' or digit=='{':
                stack.append(digit)
            elif digit==')' or digit==']' or digit=='}':
                try:
                    d = stack.pop()
                except:
                    return False
                if( (digit==')' and d!='(') or (digit==']' and d!='[') or (digit=='}' and d!='{')):
                    return False
        if stack:
            return False
        return True
