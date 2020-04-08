#backtracking sol
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def gen(s='', l=0, r=0):
            print(s)
            if len(s)==2*n:
                ret.append(s)
                return
            if l<n:
                gen(s+'(', l+1, r)
            if r<l:
                gen(s+')', l, r+1)
        gen()
        return ret
    
#END OF EFFICIENT SOL -  BACKTRACKING

#brute force
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
