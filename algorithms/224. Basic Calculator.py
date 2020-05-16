#Approach 1: Stack and String Reversal
#space and run -O(n)
class Solution:
    def calculate(self, s: str) -> int:
        def eval(stack):
            res= stack.pop() if stack else 0
            while stack and stack[-1]!=')':
                sign =stack.pop()
                if sign=='+':
                    res+=stack.pop()
                else:
                    res-=stack.pop() 
            return res
        stack = []
        n, operand = 0,0
        for i in range(len(s)-1, -1,-1):
            c = s[i]
            if c.isdigit():
                operand = (10**n*int(c)) + operand
                n+=1
            elif c!=" ":
                if n:
                    stack.append(operand)
                    n, operand =0,0
                if c=='(':
                    res =eval(stack)
                    stack.pop() #pop closing )
                    stack.append(res)
                else:
                    stack.append(c)
        if n:
            stack.append(operand)
        return eval(stack)
