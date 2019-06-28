#Myungho Sim
#hackerrank problem: staircase
#print out right adjusted staircase that consist of #s
#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    for i in range(n):
        str="#"*(i+1)
        print(str.rjust(n," "))
if __name__ == '__main__':
    n = int(input())

    staircase(n)
