# 393.utf8_validation.py
#sol: https://leetcode.com/articles/utf-8-validation/

#requirements
For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, **followed by n-1 bytes**(recursive) with most significant 2 bits being 10.
e.g  4 bytes char = [a,b,c,d]
the first n-bits of the first number are all one's for the first n bits. For the same num, it is followed by 0 at n+1 bit. 
the following numbers represent n-1 bytes. 3 byte number has [a,b,c]. each number's most significant 2 bits- last digit is 10. 
* the relationships are recursive. Nth byte number describes what's immediately behind. 

#Example 1:
data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
2 bytes char: 11000101
followed by 1bytes char :  10000010
n-1 byte=@1 byte char = 10000010 describes 1 byte num. it is followed by 00000001
