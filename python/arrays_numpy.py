#Myungho Sim
#arrays problem from hackerrank
#reverse an array with numpy and print out in float format
import numpy
def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr,float)
    return arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
