#Myungho Sim
#2d array problem from hackerrank: Find the maximum hourglass sum in the 2d array
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    nrows = len(arr)
    ncols = len(arr[0])
    max_sum = -sys.maxsize-1
    for i in range(0,nrows-2):
        for j in range(0,ncols-2):
            a= arr[i][j]
            b= arr[i][j+1]
            c= arr[i][j+2]
            d= arr[i+1][j+1]
            e= arr[i+2][j]
            f= arr[i+2][j+1]
            g= arr[i+2][j+2]
            sum = a+b+c+d+e+f+g
            if max_sum<sum:
                max_sum = sum
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
