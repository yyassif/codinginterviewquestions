def find_pair(nums, target):
    dic={}
    arr=[]
    for i,num in enumerate(nums):
        diff = target-num
        if diff in dic:
            arr.append([diff,num])
        dic[num] =i
    #get the pair with the largest number
    pair = max(arr)
    x,y = pair[0],pair[1]
    #get index of the pair and sort it 
    i,j = dic[x],dic[y]
    if i>j:
        i,j=j,i
    return [i,j]
def test_driver(input,target,result):
    print(input)
    print(target)
    ret = find_pair(input, target)
    print("expected:",result, "result:", ret)
    assert ret ==result
input = [1, 10, 25, 35, 60]
target=60
test_driver(input,target, [2,3])

input = [20, 50, 40, 25, 30, 10]
target=60
test_driver(input,target, [1,5])
