#Myungho Sim
#hackerrank problem for time conversion
#convert regular time format to military time format
#!/bin/python3

import os
import sys

# convert time format to military time format
def timeConversion(s):
    size = len(s)
    last_two = s[size-2:]
    new_hour=0
    hour_num= int(s[0:2])
    if last_two=="PM":
        # if 1pm~9pm, 10~11pm, add 12 hours)
        #1am to 11am, 12pm no change needed
        #12am -> 00 hr
        if (hour_num>=1 and hour_num<=11):
            new_hour= 12+hour_num
        else:
            new_hour = hour_num
    elif (last_two =="AM" and hour_num==12):
        new_hour = 0
    else:
        new_hour = hour_num
    new_hr_str =""
    if new_hour<10:
        new_hr_str = "0"+str(new_hour)
    else:
        new_hr_str = str(new_hour)
    s = str(new_hr_str) + s[2:size-2]
    return s

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
