#two pointer sliding window
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
            j += 1
        return total
