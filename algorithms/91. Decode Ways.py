#iterative sol run/space O(n)
#e.g. dp array for "326"
(3,2,6) is one case. (3,26) is 2nd case. that's why it's like carrying off the baton
for loop
[1, 1, 1, 0]
[1, 1, 1, 0]
for loop
[1, 1, 1, 1]
[1, 1, 1, 2]
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, n+1): #store the results from 1 or 2 digits before at i
            if s[i-1]!='0':
                dp[i] +=dp[i-1]
            two_digit = int(s[i-2:i])
            if two_digit >=10 and two_digit <=26:
                dp[i] +=dp[i-2]      #check two valid digits, store value at dp[i] from dp[i-2] 
                #b/c you count once for 1 digit and another for two digits. 
        return dp[n]
#recursive sol run/space O(n)
# '0' doesn't have a single digit decode.
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        memo = {}
        n = len(s)
        def rec(i):
            if i==n:
                return 1
            if s[i]=='0':         # '0' doesn't have a single digit decode.
                return 0
            if i==n-1:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = rec(i+1) + (rec(i+2) if int(s[i:i+2])<=26 else 0)
            return memo[i]
        return rec(0)
