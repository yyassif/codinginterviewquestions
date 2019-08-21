#Myungho Sim
#roman to integer problem at leetcode
class Solution:
    def romanToInt(self, s: str) -> int:
        size = len(s)
        v=0
        for i in range(size):
            d = s[i]
            if d=="I":
                if i==size-1 or (i<size-1 and s[i+1]=="I"):
                    v+=1
            elif d=="V":
                if i==size-1 or (i<size-1 and s[i+1]=="I"):
                    v+=5
                    if(i>0 and s[i-1]=="I"):
                        v-=1
            elif d=="X":
                if i==size-1 or (i<size-1 and (s[i+1]=="I" or s[i+1]=="V" or s[i+1]=="X")):
                    v+=10
                    if(i>0 and s[i-1]=="I"):
                        v-=1
            elif d=="L":
                if i==size-1 or (i<size-1 and (s[i+1]=="I" or s[i+1]=="V" or s[i+1]=="X" or s[i+1]=="L")):
                    v+=50
                    if(i>0 and s[i-1]=="X"):
                        v-=10
            elif d=="C":
                if i==size-1 or (i<size-1 and (s[i+1]=="I" or s[i+1]=="V" or s[i+1]=="X" or s[i+1]=="L" or s[i+1]=="C")):
                    v+=100
                    if(i>0 and s[i-1]=="X"):
                        v-=10
            elif d=="D":
                if i==size-1 or (i<size-1 and (s[i+1]=="I" or s[i+1]=="V" or s[i+1]=="X" or s[i+1]=="L" or s[i+1]=="C" or s[i+1]=="D")): 
                    v+=500
                    if(i>0 and s[i-1]=="C"):
                        v-=100
            elif d=="M":
                if i==size-1 or (i<size-1 and (s[i+1]=="I" or s[i+1]=="V" or s[i+1]=="X" or s[i+1]=="L" or s[i+1]=="C" or s[i+1]=="D" or s[i+1]=="M")): 
                    v+=1000
                    if(i>0 and s[i-1]=="C"):
                        v-=100
        return v
                
                
