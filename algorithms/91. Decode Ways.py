class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        memo= {}
        def recursive_with_memo(index) -> int:
            # If you reach the end of the string
            # Return 1 for success.
            if index == len(s):
                return 1

            # If the string starts with a zero, it can't be decoded
            if s[index] == '0':
                return 0

            if index == len(s)-1:
                return 1

            # Memoization is needed since we might encounter the same sub-string.
            if index in memo:
                return memo[index]

            memo[index]= recursive_with_memo(index+1) \
            + (recursive_with_memo(index+2) if (int(s[index : index+2]) <= 26)
             else 0)
            return memo[index]
        return recursive_with_memo(0)
