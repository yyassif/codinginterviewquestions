#Myungho Sim
#big sum problem from hackerrank
#hard implementation of big sum
#!/bin/python3
# WORK IN PROGRESS
import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum=""
    for num in ar:
        sum = bigsum(sum, num)
    return sum
def bigsum(n1, n2):
    num1= str(n1)
    num2 = str(n2)
    sum =""
    len1 = len(num1)
    len2 = len(num2)
    
    if(len2>len1): # swap num1 and num2 if num2 is bigger
        t = num1
        num1 = num2
        num1 = t
    for i in range(len2):
        digit1 = int(num1) #len1-i-2
        digit2 = int(num2)
        add_digits = digit1+digit2
        sum = sum + int(add_digits/10)
    return sum[::-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(str, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
