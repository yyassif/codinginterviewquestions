#Myungho Sim
#273.integertoenglishwords.py
class Solution:
    def numberToWords(self, num: int) -> str:
        original = num
        if num==0:
            return "Zero"
        names = ["Hundred","thousand","million","billion"]
        digits=["One", "Two", "Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
        tens = ["Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        teens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        words=[]
        loop=0 #0=less than thousand, 1=1000, 2=M, 3=B
        def lt10(n):
            if (n%10)!=0:
                d = n%10
                words.append(digits[d-1])
        def lt100(n):
            if 10<=n<20:
                d = n%10
                words.append(teens[d])
            elif n<10:
                lt10(n)
            else: #above 20
                lt10(n)
                d = (n%100)//10
                words.append(tens[d-2])
        def lt1000(n): #less than thousand
            if ((n%1000)//100)>=1: #hundreds
                lt100(n%100)
                string=""
                d = (n%1000)//100 #d hundred 
                string += digits[d-1]+" "
                string+="Hundred"
                words.append(string)
            elif (n%1000)<100:
                lt100(n)
        while num>0:
            if (num%1000) !=0:
                if loop==1:
                    words.append("Thousand")    
                elif loop==2:
                    words.append("Million")
                elif loop==3:
                    words.append("Billion")
                lt1000(num%1000)
            loop+=1
            num=num//1000
        res=""
        while words:
            res+=words.pop()+" "
        res = res[:len(res)-1]
        return res
