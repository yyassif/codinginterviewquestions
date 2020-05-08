# sol 3 dynamic programming bottom up without recursion runtime/space O(T*P)
# Also review top down method and approach 1
class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]

#approach 2 top down dynamic programming
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        memo = {}
        def dp(i,j):
            if (i, j) not in memo:   #i for text, j for pattern
                if j==len(pattern):
                    ans = i== len(text) #does the end of pattern/text reach at the same time?
                else:
                    first = i<len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*': #e.g. aaabb and a*bb
                        #a) check whether 0 of pattern[j] matches against text[i]
                        #OR b) check current j pattern against next text[i+1] e.g. a* against aaabb  
                        ans = dp(i,j+2) or first and dp(i+1,j) 
                    else:
                        ans = first and dp(i+1, j+1) #match next letters
                memo[i,j] = ans
            return memo[i,j]
        return dp(0,0)
            
# Approach 1: Recursion  runtime O( (T+P)*2^(T+P/2) ) , space O(T^2+P^2)
#https://leetcode.com/articles/regular-expression-matching/
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        if len(pattern)>=2 and pattern[1]=="*":
            return self.isMatch(text, pattern[2:]) or\
            first_match and self.isMatch(text[1:], pattern)
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
