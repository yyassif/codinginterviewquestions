#Myungho Sim
# reference - regex: http://regexlib.com/Search.aspx?k=phone&AspxAutoDetectCookieSupport=1
# Read from the file file.txt and output all valid phone numbers to stdout.
input="file.txt"
while IFS= read -r line;
do
    if [[ $line =~ ^((\([0-9]{3}\) )|[0-9]{3}-)[0-9]{3}-[0-9]{4}$ ]];
    then
        echo "$line"
    fi
done < "$input"
