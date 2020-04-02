#Amazon OA question : https://leetcode.com/discuss/interview-question/370112
#brute force
s = "abcabc"
k = 3
n = len(s)
ret = []
for i in range(n-k+1):
    map = {}
    for j in range(k):
        c = s[i+j]
        if c in map:
            break
        else:
            map[c] = 1
    print(s[i:i+k])
    if len(map)==k and s[i:i+k] not in ret:
        ret.append(s[i:i+k])
print(ret)
