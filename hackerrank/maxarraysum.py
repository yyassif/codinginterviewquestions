#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    size = len(arr)
    dp = []
    dp.append(max(0,arr[0]))
    dp.append(max(dp[0], arr[1]))
    if size==1:
        return dp[0]
    for i in range(2, size):
        prev = dp[-1]
        curr = dp[-2]+arr[i]
        dp.append(max(dp[-2], max(prev, curr)))
    return max(dp[-2], dp[-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
