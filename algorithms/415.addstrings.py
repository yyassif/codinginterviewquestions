#415 add strings 
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2)>len(num1):
            num1,num2 = num2,num1
        s1=len(num1)
        s2=len(num2)
        d=0
        c=0
        num=""
        for i in range(1,s2+1):
            d = (int(num1[-i])+int(num2[-i])+c) %10
            num+= str(d)
            c = (int(num1[-i])+int(num2[-i])+c) //10
        print(num)
        if s1>s2:
            for i in reversed(range(0,s1-s2)):
                # if i== (s1-s2-1):
                print("> ",num1[i])
                t=(int(num1[i])+c)%10
                c=(int(num1[i])+c)//10
                num+=str(t)
                # else:
                #     print("else",num1[i])
                #     num+=num1[i]
        if c==1:
            num+="1"
        return num[::-1]
