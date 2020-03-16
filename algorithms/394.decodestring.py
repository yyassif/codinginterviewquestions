#394.decodestring.py
#sol adopted from https://leetcode.com/problems/decode-string/discuss/508115/Simple-python-with-stack-easy-to-understand
class Solution:
    def decodeString(self, s: str) -> str:
        size= len(s)
        if size==0:
            return ""
        stack = []
        
        for i in range(size):
            cur=s[i]
            if cur=="[" or cur.isdigit() or cur.isalpha():
                stack.append(cur)
            else: # ] encountered
                pat=""
                while stack and stack[-1].isalpha():
                    pat = stack.pop()+pat
                stack.pop() #rid of [
                k_str=""
                while stack and stack[-1].isdigit():
                    k_str = stack.pop()+k_str
                k=int(k_str)
                stack.append(pat*k)
        return ''.join(stack)
