# Myungho Sim
# hackerank interview problem
# problem : Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = ()
    for num in integer_list:
        t = t + (num,)
    print(hash(t))
