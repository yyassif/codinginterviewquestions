# 139. Word Break from leetcode
#brute force solution - passes some cases,time limit exceeded
s = "cars"
wordDict = ["car","ca","rs"]
size = len(s)
start=0
found = False
def rec(start):
    if start==size:
        return True
    end = start+1
    for end in range(start, size+1):
        print(start,end)
        if s[start:end] in wordDict and rec(end):
            return True
    return False
print(rec(0))
