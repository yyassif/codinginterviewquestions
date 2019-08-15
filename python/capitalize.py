#Myungho Sim
#capitalize problem from hackkerank
#capitalize the first letter after a space in a string
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    idx=0
    n = len(s)
    first=True
    while idx<n:
        if s[idx]==' ':
            idx+=1
            first=True
            continue
        elif first==True:
            s = s[:idx]+s[idx].upper()+s[idx+1:]
            first=False
        idx+=1
    return s        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
