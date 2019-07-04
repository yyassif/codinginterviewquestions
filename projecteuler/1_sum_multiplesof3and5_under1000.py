#Myungho Sim
#sum multiples of 3 and 5 under 1000
max = 1000
sum =0
for i in range(0, max):
  if (i%3 ==0) or (i%5==0):
    sum+=i
  else:
    continue
print("sum of integers below ",max," : ",sum)
#output 
#sum of integers below  1000  :  233168
