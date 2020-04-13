#sol 1
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                j = n // i
                if ''.join([s[:i]] * j) == s:
                    return True
        return False

#########################################################

#sol 2
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]
