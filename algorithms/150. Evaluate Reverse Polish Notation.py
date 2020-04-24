#do not truncate towards 0 with division, 
#e.g. 3//-2  = -2
def evalRPN(self, tokens):
    
    stack = []
    
    for token in tokens:
        
        if token not in "+-/*":
            stack.append(int(token))
            continue
    
        number_2 = stack.pop()
        number_1 = stack.pop()
        
        result = 0
        if token == "+":
            result = number_1 + number_2
        elif token == "-":
            result = number_1 - number_2
        elif token == "*":
            result = number_1 * number_2
        else:  # DO NOT USE num1//num2. USE int(num1/num2) like below!!!!!!!!!!!!!!!!!!!!!
            result = int(number_1 / number_2)   #VERY IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!
            
        stack.append(result)

    return stack.pop()
