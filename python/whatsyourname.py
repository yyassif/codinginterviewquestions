#Myungho Sim
#hackerrank problem : what's your name
def print_full_name(a, b):
    str = "Hello " + a+" "+ b+ "! You just delved into python."
    print(str)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
