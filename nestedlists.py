# author: Myungho Daniel Sim
# Nested list question 
# source hackerrank.com
# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
list = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    item = [name, score]
    list.append(item)
list.sort(key = lambda x: x[1]) 
size = len(list)
idx = 0
#increment first idx
score = list[0][1]
while True:
    idx+=1
    if(score== list[idx][1]):
        score= list[idx][1]
        continue
    else:
        break

second_score = list[idx][1]
second_name = list[idx][0]
names = []
names.append(second_name)
while idx<size-1:
    idx+=1
    if(list[idx][1]==second_score):
        second_name = list[idx][0]
        names.append(second_name)
    else:
        break
names.sort()
for n in names:
    print(n) 
