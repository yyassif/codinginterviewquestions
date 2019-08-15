#Myungho Sim
#Your task is to use for loops to display only odd natural numbers from 1 to 99.
#!/bin/bash
#version 1
for i in {1..99..2}
  do 
     echo $i
 done

#version 2
for i in {1..99}
  do 
    if (($i%2==0)); then
        continue
    else
        echo $i
    fi
 done

