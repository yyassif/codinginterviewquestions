#Myungho Sim
#designer door mat problem from hackerrank
#draw welcome mat in python
a = input().split()
n = int(a[0])
m = int(a[1])
pat = ".|."
fill = "-"
welcome = "WELCOME"
for i in range(1,n-1,2):
    print((pat*i).center(m,fill))
print(welcome.center(m,fill))
for i in range(n-2,0,-2):
    print((pat*i).center(m,fill))
