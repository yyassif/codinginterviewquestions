#greedy  run-O(n), space - O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(a,b):
            for i in range(a,b):
                if s[i]!=s[b-i+a]:
                    return False
            return True
        n=len(s)
        success=True
        for i in range(n//2):
            if s[i]!=s[~i]:
                j=n-i-1
                return valid(i+1,j) or valid(i,j-1)
        return True
#brute force time limit exceeded, time- O(n^2), space - O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(string):
            n = len(string)
            for i in range(n//2):
                if string[i]!=string[n-i-1]:
                    return False
            return True
        if valid(s):
            return True
        else:
            if valid(s[1:]):
                return True
            for i in range(1,len(s)):
                new_s = s[:i]+s[i+1:]
                if valid(new_s):
                    return True
        return False
