#Myungho Sim
#noidea problem from hackerrank
#for given array, increment 1 if a number is found in set A and decrement -1 if found in b
m,n = map(int, input().split())
arr = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))
score=0
for i in arr:
    if i in a:
        score+=1
    if i in b:
        score-=1
print (score)


