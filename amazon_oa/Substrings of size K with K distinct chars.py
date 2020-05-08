#Amazon OA question : https://leetcode.com/discuss/interview-question/370112
#Python solution based on an easier problem LeetCode 1358
def find_substring(s, k):
    record = {}
    res = idx = cnt = 0
    removed = '#'
    for i in range(len(s)):
        if s[i] != removed:
            cnt = 0
        record[s[i]] = record.get(s[i], 0) + 1
        if len(record) == k:
            while len(record) == k:
                record[s[idx]] -= 1
                if record[s[idx]] == 0:
                    removed = s[idx]
                    del record[s[idx]]
                idx += 1
                cnt += 1
            res += cnt
    return res


def test_driver(s,k, result):
    ret = find_substring(s, k)
    print(s,k,result)
    print("resut :", ret)
    print("expected: ",result, end="\n\n")
    assert ret==result
test_driver("pqpqs", 2, 7)
test_driver("aabab", 3,0)

