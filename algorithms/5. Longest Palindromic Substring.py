#5. Longest Palindromic Substring

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
