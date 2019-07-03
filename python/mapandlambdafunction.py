#Myungho Sim
#hackerrank problem
#map and lambda function - return fibonacci number cubed
cube = lambda x: x*x*x 

def fibonacci(n):
    if n==0:
        arr = []
        return arr
    elif n==1:
        arr = [None]*1
        arr[0] = 0
        return arr 
    # return a list of fibonacci number
    arr = [None]*n
    arr[0] = 0
    arr[1] = 1
    for i in range(2,n):
        arr[i] = arr[i-2] + arr[i-1]
    size = len(arr)
    return arr

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
