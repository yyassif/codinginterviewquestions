#iterative sol run/space O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, n+1):
            if s[i-1]!='0':
                dp[i] +=dp[i-1]
            two_digit = int(s[i-2:i])
            if two_digit >=10 and two_digit <=26:
                dp[i] +=dp[i-2]
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
