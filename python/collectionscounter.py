#Myungho Sim
# hackerrank problem: collections.Counter()
# His shop has  number of shoes. 
# He has a list containing the size of each shoe he has in his shop. 
# There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.
# Your task is to compute how much money  earned.
# Enter your code here. Read input from STDIN. Print output to STDOUT
n_sizes = int(input())
sizes = list(map(int, input().split()))
n_customers = int(input())
sum =0
set_prices = []
for i in range(n_customers):
    line = input().split()
    size = int(line[0])
    price = int(line[1])
    if size in sizes:
        sizes.remove(size)
        sum+=price

print(sum)


