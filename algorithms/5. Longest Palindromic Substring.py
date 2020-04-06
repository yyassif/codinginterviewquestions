#5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if s is None and n==0:
            return None
        start=0
        end=0
        def expand(a,b):
            while 0<=a and b<n and s[a]==s[b]:
                a-=1
                b+=1
            print("a b",a,b,b-a-1) #expands to a=-1 and b==n
            return b-a-1
        for i in range(n):
            len1 = expand(i,i)   #grow i to the left when i>0
            len2 = expand(i,i+1) # allow i to grow to the right when i=0
            maxi = max(len1, len2) #find max center length
            if maxi>end-start: #update max center start, end
                #e.g maxi is 3 when len(substr)==5 and 4 when len(substr)==6
                #e.g. if maxi=3, i=3,start=0 and end=
                start = i-(maxi-1)//2   
                end = i+maxi//2
            print("1,2,m,s,e,sub",n1,n2,maxi,start,end,s[start:end+1])
        return s[start:end+1]
        
            
                
                
                

#brute force time limit exceeded
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def valid(sub):
            sn=len(sub)
            for i in range(sn//2):
                if sub[i]!=sub[sn-i-1]:
                    return False
            return True
        n=len(s)
        maxi=0
        maxi_str=""
        for i in range(n):
            for j in range(1,n+1):
                substr=s[i:j]
                # print(substr)
                if valid(substr):
                    if maxi<len(substr):
                        maxi = len(substr)
                        maxi_str = substr
                    
        return maxi_str 
