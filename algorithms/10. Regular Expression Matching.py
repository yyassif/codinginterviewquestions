# Approach 1: Recursion  runtime O( (T+P)*2^(T+P/2) ) , space O(T^2+P^2)

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
