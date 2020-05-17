#recursive sol run/space O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        memo = {}
        n = len(s)
        def rec(i):
            if i==n:
                return 1
            if s[i]=='0':
                return 0
            if i==n-1:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = rec(i+1) + (rec(i+2) if int(s[i:i+2])<=26 else 0)
            return memo[i]
        return rec(0)
