#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    h.append(0)
    i=0
    area=0
    stack = []
    while i<len(h):
        if not stack or h[stack[-1]]<=h[i]:
            stack.append(i)
            i+=1
        else:
            top = stack.pop() 
            area = max(area, h[top]*(i-stack[-1]-1 if stack else i))
    return area
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
