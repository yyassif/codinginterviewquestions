#Amazon OA  Optimal Utilization
#from https://leetcode.com/discuss/interview-question/373202
def findPairs(a, b, target):
	a.sort(key=lambda x: x[1])
	b.sort(key=lambda x: x[1])
	l, r = 0, len(b) - 1
	ans = []
	curDiff = float('inf')
	while l < len(a) and r >= 0:
		id1, i = a[l]
		id2, j = b[r]
		if (target - i - j == curDiff):
			ans.append([id1, id2])
		elif (i + j <= target and target - i - j < curDiff): #found new pair whose sum is closer to the target than previous ones
			ans.clear()
			ans.append([id1, id2])
			curDiff = target - i - j
		if (target > i + j):
			l += 1
		else:
			if target == i + j:
				tmp_l = l
				while a[tmp_l][1] + b[r][1] == target:
					tmp_l += 1
					if tmp_l == len(a):
						break
					if  a[tmp_l][1] + b[r][1] == target:
						ans.append([a[tmp_l][0], b[r][0]])
			r -= 1
	
	ans.sort(key = lambda x: x[1])
	ans.sort(key = lambda x: x[0])
	return ans

# test 1
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7
expected = [[2, 1]]
assert findPairs(a, b, target) == expected

# test 2
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20
expected = [[3, 1]]
assert findPairs(a, b, target) == expected

# test 3
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20
expected = [[1, 3], [3, 2]]
assert findPairs(a, b, target) == expected

# test 4
a = [ [1, 5], [2, 5] ]
b = [ [1, 5], [2, 5] ]
target = 10
expected = [[1, 1], [1, 2], [2, 1], [2, 2]]
assert findPairs(a, b, target) == expected

a, b, target = [ [1, 5], [2, 5] ], [ [1, 5], [2, 5] ], 10
expected= [[1, 1], [1, 2], [2, 1], [2, 2]]
assert findPairs(a,b,target) == expected
###########################END OF EFFICIENT SOL

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
