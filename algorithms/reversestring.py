#Myungho Sim
#reverse string in place @ leet code
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        for i in range(int(size/2)):
            temp = s[i]
            s[i] = s[size-1-i]
            s[size-1-i] = temp
