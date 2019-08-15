#Myungho Sim
#string formatting problem from hackeerank
#formatting source: https://pyformat.info/
def print_formatted(number):
    n = int(number)
    w=len(bin(n)[2:])
    # your code goes here
    for i in range (1,n+1):
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))

#optional implementation
#convert base 10 to any base specified by base
#input n=decimal number, base=resulting number base
def convertbase(n,base):
    result =""
    while n !=0:
        mod = n%base
        if base==16:
            if(mod==10):
                result = result + "A"
            elif(mod==11):
                result = result + "B"
            elif(mod==12):
                result = result + "C"
            elif(mod==13):
                result = result + "D"
            elif(mod==14):
                result = result + "E"
            elif(mod==15):
                result = result + "F"
            else:
                result = result +str(mod)    
        else:
            result = result +str(mod)
        n = n // base
        
    return result[::-1]


if __name__ == '__main__':
