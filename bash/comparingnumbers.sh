#Myungho Sim
#comparing numbers
#bash cheatsheet https://devhints.io/bash
read x
read y
if (($x<$y));then
    echo X is less than Y 
elif (($x == $y));then
    echo X is equal to Y 
elif (($x > $y));then
    echo X is greater than Y 
fi
