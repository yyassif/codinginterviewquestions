#Myungho Sim
#hackerrank problem on exceptions
#detect valueerror and divide by zero error when integer dividing
n = int(input())
for i in range(n):
    val=0
    try:
        a,b = map(int, input().split())
        val = a//b
        print(val)       
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
    


