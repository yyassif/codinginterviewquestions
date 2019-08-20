#Myungho Sim
#count and say problem @leetcode
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        a="1"
        newstr=""
        if n==1:
            return "1"
        for j in range(n-1):
            newstr = ""
            size = len(a)
            digit=""
            if size==1:
                newstr = "1"+a
            else:
                cnt=1
                for i in range(size-1):
                    if a[i]==a[i+1]:
                        cnt+=1
                    elif a[i]!=a[i+1]:
                        digit = a[i]
                        newstr += str(cnt)+digit
                        cnt=1
                newstr += str(cnt) + a[size-1]
            a = newstr
            print(a)
        return newstr
