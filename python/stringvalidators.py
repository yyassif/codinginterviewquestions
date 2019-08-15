#Myungho Sim
#string validators problem from hackerank
#Python has built-in string validation methods for basic data. 
#It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
if __name__ == '__main__':
    s = input()
    checkalnum = False
    checkalpha = False
    checkdigit = False
    checklower = False
    checkupper = False
    for digit in s:
        if digit.isalnum():
            checkalnum =True
        if digit.isalpha():
            checkalpha = True
        if digit.isdigit():
            checkdigit = True
        if digit.islower():
            checklower = True
        if digit.isupper():
            checkupper = True
    if checkalnum==True:
        print ("True")
    else:
        print ("False")
    
    if checkalpha==True:
        print ("True")
    else:
        print ("False")
    
    if checkdigit==True:
        print ("True")
    else:
        print ("False")
    
    if checklower==True:
        print ("True")
    else:
        print ("False")
    
    if checkupper==True:
        print ("True")
    else:
        print ("False")
