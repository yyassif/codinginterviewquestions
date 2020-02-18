# 393.utf8_validation.py
#sol: https://leetcode.com/articles/utf-8-validation/

#requirements
For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, **followed by n-1 bytes** with most significant 2 bits being 10.
e.g  4 bytes char = [a,b,c,d]
the first n-bits of the first number are all one's for the first n bits. For the same num, it is followed by 0 at n+1 bit. 
the following numbers represent n-1 bytes. 3 byte number has [a,b,c]. each number's most significant 2 bits- leftmost digits are 10. 
*  Nth byte number describes what's immediately behind. 

#Example 1:
data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
2 bytes char: 11000101
followed by 1bytes char :  10000010
n-1 byte=@1 byte char = 10000010 describes 1 byte num. it is followed by 00000001

#SOLUTION from https://leetcode.com/problems/utf-8-validation/discuss/87530/Python-Easy-to-understand-Solution
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        if not data:
            return False
        i=0
        n = len(data)
        arr = [bin(x)[2:].zfill(8) for x in data]
        #valid cases of leading 1's for N bytes
        # 11 000000    
        # 111 00000
        # 1111 0000
        while i<n:
            num = arr[i]
            cnt = len(arr)- len(num.lstrip('1')) #count length after leading 1's
            if cnt==0:
                i+=1
            elif 2<=cnt<=4: #make sure N byte cnt is between 2 and 4
                #check next number if begins with 10 and remaining cnt is 1 or greater
                while i+1<n and arr[i+1].startswith('10') and cnt>1: 
                    i+=1
                    cnt-=1
                #check if leading number encodes Nbytes but there are less than N continuous numbers. 
                #e.g. 11100000 followed by 00000001
                if cnt!=1: 
                    return False
                i+=1
            else:
                return False
        return True
        
                
