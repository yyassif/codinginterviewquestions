#1239. Maximum Length of a Concatenated String with Unique Characters
#sol adapted from https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/513327/Simple-Backtracking-solution
#backtracking solution
#TIME LIMIT EXCEEDED
class Solution:
    def __init__(self):
        self.maxi=0
    def maxLength(self, arr: List[str]) -> int:
        string=""
        def is_unique(text):
            map={}
            for t in text:
                if t in map:
                    return False
                else:
                    map[t]=1
        def dfs(start,string):
            if is_unique(string)==False:
                return 
            self.maxi = max(self.maxi, len(string))
            for i in range(start, len(arr)):
                dfs(start+1, string+arr[i])
        dfs(0, "")
        return self.maxi
