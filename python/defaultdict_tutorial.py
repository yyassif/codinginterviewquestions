#Myungho Sim
#default dict tutorial from hackerank
#read input for list a and b
#check if items in b are in a and print indexes of a. otherwise print -1
#ideas taken from discussions board
from collections import defaultdict
n,m = map(int, input().split())
a_dict = defaultdict(list)
#map input for a_dict
for i in range(n):
    next_char = input()
    a_dict[next_char].append(str(i+1))
#iterate through list b and check for list a
for i in range(m):
    next_char = input()
    print(" ".join(map(str, a_dict[next_char])) or -1)
