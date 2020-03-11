#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    dict = {}
    lefts = "({["
    rights = ")}]"
    dict[")"] = "("
    dict["}"] = "{"
    dict["]"] = "["
    stack = []
    for br in s:
        if br in lefts:
            stack.append(br)
        elif br in rights:
            if not stack or stack.pop()!=dict[br]:
                return "NO"
    return "YES" if not stack else "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
