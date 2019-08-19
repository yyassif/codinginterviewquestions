#Myungho Sim
#valid palindrome 2 from leetcode
#better than 93% of submissions
import re
class Solution(object):
    def isPalindrome(self,s):
        s = re.sub("[^a-zA-Z0-9]+","",s).lower()
        size = len(s)
        for i in range(int(size/2)):
            if(s[i]!=s[size-1-i]):
                return False
        return True
