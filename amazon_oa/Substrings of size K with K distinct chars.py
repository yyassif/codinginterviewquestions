#Amazon OA question : https://leetcode.com/discuss/interview-question/370112
#efficient sol
#solution same as 3. Longest Substring Without Repeating Characters except it checks for lengths=k and adds it to a set
s = "abcabc"
k = 3
def substringk(s, k):
    n = len(s)
    if n<k or k == 0:
        return []
    
    map, res = {}, set()
    i = 0
    for j in range(n):
        c= s[j]
        if c in map:
            i = map[c]+1
        map[c] = j
        if j-i+1==k:   #
            res.add(s[i:j+1])
            i += 1
    return list(res)
ret = substringk(s,k)
print(ret)
######################examples
Example 1:

Input: s = "pqpqs", k = 2
Output: 7
Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
Example 2:

Input: s = "aabab", k = 3
Output: 0

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
