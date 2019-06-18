#Myungho Sim
#hackerank easy problem - compare the triplets
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_score =0
    b_score =0 
    for i,j in zip(a,b):
        if(i>j):
            a_score +=1
        elif(i<j):
            b_score +=1
    return (a_score,b_score)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
