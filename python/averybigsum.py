#Myungho Sim
#big sum problem from hackerrank
#hard implementation of big sum. Not necessary in python but for practice
#!/bin/python3
# idea taken from geeksforgeeks article #https://www.geeksforgeeks.org/sum-two-large-numbers/
import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    sum=""
    for num in ar:
        sum = bigsum(sum, str(num))
    return sum
def bigsum(n1, n2):
    num1= str(n1)
    num2 = str(n2)
    sum =""
    len1 = len(num1)
    len2 = len(num2)
    carry=0
    if(len1>len2): # swap num1 and num2 if num2 is bigger
        t = num2
        num2 = num1
        num2 = t
    len1 = len(num1)
    len2 = len(num2)
    diff = len2-len1 # to find correct index for len2 which is longer
    # decrease by 1. add from one's digits first
    for i in range(0, len1): #len2-1,-1,-1
        digit1 = int(num1[len1-i-1]) #len1-i-2
        digit2 = int(num2[len2-i-1+diff]) 
        add_digits = digit1+digit2 + carry
        carry = add_digits//10
        sum = sum + str(add_digits%10)
    for i in range(len1,len2):
        digit2 = int(num2[len2-i-1]) 
        add_digits = digit2+carry
        carry = add_digits//10
        sum = sum + str(add_digits%10)
    if(carry):
        sum = sum+ str(carry)
    return sum[::-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(str, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
