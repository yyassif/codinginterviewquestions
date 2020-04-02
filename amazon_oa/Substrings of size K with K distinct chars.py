#Amazon OA question : https://leetcode.com/discuss/interview-question/370112
#more efficient sol
s = "abcabc"
k = 3
n = len(s)
def substringk(s, k):
    if not s or k == 0:
        return []
    
    letter, res = {}, set()
    start = 0
    for i in range(len(s)):
        if s[i] in letter and letter[s[i]] >= start:
            start = letter[s[i]]+1
        letter[s[i]] = i
        if i-start+1 == k:
            res.add(s[start:i+1])
            start += 1
    return list(res)
ret = substringk(s,k)
print(ret)


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
