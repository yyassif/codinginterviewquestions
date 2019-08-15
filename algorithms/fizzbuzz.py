#Myungho Sim
#fizzbuzz problem
#print Fizz when multiples of 3, Buzz when multiples of 5, if both, print FizzBuzz, otherwise, print number. 
#run program for numbers 1 to 100.
for i in range(1,101):
    if( (i % 3==0) and (i %5==0)):
        print('FizzBuzz')
    elif ( (i % 3==0) and (i %5!=0)):
        print('Fizz')
    elif ( (i % 3!=0) and (i %5==0)):
        print('Buzz')
    else:
        print (i)
