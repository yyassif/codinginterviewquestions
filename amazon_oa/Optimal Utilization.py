#Amazon OA  Optimal Utilization
#brute force
def find_optimal_utilization(a,b,target):
    arr= []
    for a_idx, a_val in a:
        for b_idx, b_val in b:
            sumv = a_val+b_val
            if sumv<=target:
                arr.append((a_idx,b_idx,sumv))
    arr.sort(key=lambda x:x[2], reverse=True)
    ret= [[x[0],x[1]] for x in arr if x[2]==target]
    if len(ret)==0:
        a, b, val = arr[0]
        ret= [[a,b]]
    print(ret)
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7
find_optimal_utilization(a,b,target)
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10
find_optimal_utilization(a,b,target)
