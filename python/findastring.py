#Myungho Sim
#find a string problem from hackerrank
#count how many substrings appear in a given string
def count_substring(string, sub_string):
    sub_size = len(sub_string)
    size = len(string)
    count =0 
    for i in range(0, size-sub_size+1):
        if(string[i:i+sub_size]==sub_string):
            count+=1
    return count 
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
