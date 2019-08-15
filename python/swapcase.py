# Myungho Sim
# hackerrank swapcase problem
# You are given a string and your task is to swap cases. In other words,
# convert all lowercase letters to uppercase letters and vice versa.
def swap_case(s):
    n = len(s) 
    for i in range(n):
        if s[i].islower():
            s = s[0:i]+s[i].upper()+s[i+1:]
        else:
            s = s[0:i]+s[i].lower()+s[i+1:]
    return s    

if __name__ == '__main__':
