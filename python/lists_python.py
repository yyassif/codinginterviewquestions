# Myungho Sim
# coding problem from hackerrank
# Initialize your list and read in the value of  followed by  lines of commands 
# where each command will be of the  types listed above. Iterate through each 
# command in order and perform the corresponding operation on your list.
if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        line = input()
        tokens = line.split()
        cmd = tokens[0]
        if(cmd=="insert"):
            a = int(tokens[1])
            b = int(tokens[2])
            list.insert(a,b) 
        elif(cmd=="print"):
            print(list)
        elif(cmd=="remove"):
            val = int(tokens[1])
            try:
                list.remove(val)
            except:
                print("no val found")
        elif(cmd=="append"):
            val = int(tokens[1])
            list.append(val)
        elif(cmd=="sort"):
            list.sort() 
        elif(cmd=="pop"):
            val = list.pop() 
        elif(cmd=="reverse"):
            list.reverse()
