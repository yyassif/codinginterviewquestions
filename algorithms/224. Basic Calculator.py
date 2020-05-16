#sol 2 without reversing string
#+, - ) marks the end of operand
#runtime O(n), space O(n)
class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative  

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)  
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1   #also sign, res is appended to stack
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand
    
    
###############################################


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
