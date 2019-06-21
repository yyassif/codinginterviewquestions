#Myungho Sim
#hackrrank problem : wrap text
#wrap text by max_width size and return string
import textwrap

def wrap(string, max_width):
    n = len(string)
    result =""
    for i in range(0,n-max_width, max_width):
        result = result + string[i:i+max_width] + "\n"
    result = result + string[i+max_width:n]
    return result
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
