#Myungho Sim
# Read from the file file.txt and output the tenth line to stdout.
#bash solution
input="file.txt"
count=0
while IFS= read -r line
do
    count=$((count+1))
    if [ $count -eq 10 ]
    then
        echo "$line"
    fi
done < $input

#following solutions taken from leetcode discussions
#one line solution 1
#head -n 10 file.txt | tail -n +10

#one line solution 2
#awk 'NR==10' file.txt

#one line solution 3
sed -n 10p file.txt
