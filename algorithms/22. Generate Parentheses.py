class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret= []
        def gen(s=[]):
            if len(s)==n*2:
                if valid(s):
                    ret.append(''.join(s))
            else:
                s.append('(')
                gen(s)
                s.pop()
                s.append(')')
                gen(s)
                s.pop()
            
        def valid(s):
            cnt=0
            for c in s:
                if c=="(":
                    cnt+=1
                else:
                    cnt-=1
                if cnt<0:
                    return False
            return cnt==0
        gen()
        return ret
