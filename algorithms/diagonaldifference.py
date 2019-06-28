#Myungho Sim
#diagonal difference problem from hackkerank
#solve absolute difference between left right diagonal and right left diagonal sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    nrows = len(arr)
    ncols = len(arr[0])
    left_right_d =0
    right_left_d=0
    for i in range(nrows):
        left_right_d += arr[i][i]
        right_left_d += arr[i][nrows-i-1]
    return abs(left_right_d-right_left_d)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
