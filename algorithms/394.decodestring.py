#394.decodestring.py
#sol adopted from https://leetcode.com/problems/decode-string/discuss/508115/Simple-python-with-stack-easy-to-understand
class Solution:
    def decodeString(self, s: str) -> str:
        size=len(s)
        if size==0:
            return ""
        stack=[]
        cur=""
        for i in range(size):
            cur = s[i]
            if cur.isdigit() or cur.isalpha() or cur=="[":
                stack.append(cur)
            else:
                #get pattern 
                pat=""
                while stack and stack[-1]!='[':
                    pat = stack.pop() +pat
                stack.pop() #rid of ]
                
                #get k val
                k_str=""
                while stack and stack[-1].isdigit():
                   k_str= stack.pop()+k_str
                k = int(k_str)
                word = pat*k
                stack.append(word)
        return ''.join(stack)
                    
