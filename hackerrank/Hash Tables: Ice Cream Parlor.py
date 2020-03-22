#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    dict ={}
    n=len(cost)
    for i in range(n):
        diff = money-cost[i]
        if diff in dict:
            idx = dict[diff]
            n1= idx+1
            n2 = i+1
            if n1>n2:
                n1,n2= n2,n1
            print(n1,n2)
        dict[cost[i]] = i
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
