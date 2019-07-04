#Myungho Sim
#hackerank problem: min max sum problem
#print min max sum of 4 numbers in an array
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min=0
    max=0
    arr.sort()
    size = len(arr)
    for n in range(0,4):
        min +=arr[n]
        max +=arr[size-n-1]
    print(min,max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
