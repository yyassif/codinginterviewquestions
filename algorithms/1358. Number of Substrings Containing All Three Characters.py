#two pointer sliding window
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are 
# "abc"    (4)
# "abca"
# "abcab"
# "abcabc"
#  "bca"    (3)
#  "bcab"
#  "bcabc"
#   "cab"  (2)
#   "cabc"
#    "abc" (1)
# total = 10 = 4+3+2+1
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        total = 0
        counts = {c:0 for c in s}
        if len(counts)<3:
            return 0
        i, j = 0, 0
        while j<len(s) and i<len(s)-2:
            counts[s[j]] += 1
            while all(counts.values()): #contains all three chars
                total += len(s) - j
                counts[s[i]] -= 1
                i += 1
            j += 1 #moves to idx j so that at least one of each letter is in a substring
        return total
