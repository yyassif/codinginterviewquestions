#hackerank
#arrays left rotation
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    size = len(a)
    temp=[]
    for i in range(d):
        temp.append(a[i])
    for i in range(d,size):
        a[i-d] = a[i]
    diff= size-d
    for i in range(d):
        a[i+diff] = temp[i]
    return a
#less efficient sol
# def rotLeft(a, d):
#     size = len(a)
#     for i in range(d):
#         temp = a[0]
#         for j in range(1,size):
#             a[j-1] = a[j]
#         a[size-1] = temp
#     return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
