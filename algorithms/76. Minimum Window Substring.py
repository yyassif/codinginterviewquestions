#optimized sliding window sol 2
#space/run time O(S+T)
import collections
class Ans:
    def __init__(self):
        self.mini = float('inf')
        self.left=0
        self.right=0
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dic_t = collections.Counter(t)
        required = len(dic_t)
        filtered_s = []
        for i, char in enumerate(s):
            if char in dic_t:
                filtered_s.append((i, char))
        l, r=0,0
        formed=0
        window_counts={}
        ans = Ans()
        while r<len(filtered_s):
            c = filtered_s[r][1]
            window_counts[c] = window_counts.get(c, 0)+1
            if window_counts[c]==dic_t[c]:
                formed+=1
            while l<=r and formed==required:
                c = filtered_s[l][1]
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end-start+1<ans.mini:
                    ans.mini = end-start+1
                    ans.left = start
                    ans.right = end
                window_counts[c] -=1
                if window_counts[c] <dic_t[c]:
                    formed-=1
                l+=1
            r+=1
        return s[ans.left:ans.right+1] if ans.mini!=float('inf') else ""
    
###################################################################################
#sliding window sol 1
import collections
def minWindow(s, t):
    if not t or not s:
        return ""

    # Dictionary which keeps a count of all the unique characters in t.
    dict_t = collections.Counter(t)  #count frequency of chars of pattern T

    # Number of unique characters in t, which need to be present in the desired window.
    required = len(dict_t)    #count # of unique chars in the pattern T

    # left and right pointer
    l, r = 0, 0

    # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
    formed = 0

    # Dictionary which keeps a count of all the unique characters in the current window.
    window_counts = {}

    # ans tuple of the form (window length, left, right)
    ans = float("inf"), None, None

    while r < len(s):

        # Add one character from the right to the window
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r and formed == required:
            character = s[l]

            # Save the smallest window until now.
            if r - l + 1 < ans[0]:  #update minimum window lenght, ans =(window length, left, right)
                ans = (r - l + 1, l, r)

            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[character] -= 1
            # window_counts[c] < dict_t[c] will become eventually true since window_counts[character] -= 1
            # but there can also be multiple of the same chars as the left most char
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1 #due to contraction of the range, formed=frequency chars also decrease

            # Move the left pointer ahead, this would help to look for a new window.
            l += 1

        # Keep expanding the window once we are done contracting.
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
######################
#test driver
s = "ADOBECODEBANC"
t = "ABC"
ret= minWindow(s,t)
print("min range",ret)
