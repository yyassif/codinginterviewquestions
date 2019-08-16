#Myungho Sim
#longestCommonPrefix problem from leetcode
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        size = len(strs)
        if(size==1):
            return strs[0]
        minSize = len(strs[0])
        for i in range(size):
            if minSize> len(strs[i]):
                minSize =len(strs[i])
        lastIdx=0
        misMatch=False
        for i in range(minSize):
            letter = strs[0][i]
            for j in range(1,size):
                if strs[j][i]!=letter:
                    misMatch=True
                    break
            if(misMatch==True):
                break
            lastIdx+=1
        return strs[0][0:lastIdx]
                
        
