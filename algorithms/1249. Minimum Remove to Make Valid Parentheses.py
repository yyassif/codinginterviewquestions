class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]  #store idx of "(" in s
        remove=[]
        for i,c in enumerate(s):
            if c=="(":
                stack.append(i)
            elif c==")":  #pop "(" idx from stack
                try:
                    idx = stack.pop()
                except:
                    remove.append(i) #when stack is empty, open parenthesis "(" is missing. parenthesis is mismatched. remove idx of ")"
        #check if any unmatched "("'s are in stack - missing ")" in s
        if stack:
            for item in stack:
                remove.append(item)
        ret=""
        #remove mismatching parenthesis from s
        for i in range(len(s)):
            if i in remove:
                continue
            else:
                ret+=s[i]
        return ret
                
