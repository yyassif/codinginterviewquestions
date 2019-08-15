#Myungho Sim
#introduction to sets problem from hackerrank
#find the average from distinct values in a set
def average(array):
    # your code goes here
    setdata = set(array) # convert list to a set
    sum =0
    count =0
    for item in setdata:
        count+=1
        sum += item
    return sum/count
        
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
