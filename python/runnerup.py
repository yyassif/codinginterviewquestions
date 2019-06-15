# Myungho Daniel Sim
# description :Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    line =input().split()
    nums = {}
    for s in line:
        num = int(s)
        nums[num] = 1 
    runnerup = sorted(nums.keys())[-2]
    print(runnerup)
