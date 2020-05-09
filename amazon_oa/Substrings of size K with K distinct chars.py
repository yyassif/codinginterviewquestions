#Amazon OA question : https://leetcode.com/discuss/interview-question/370112
#problem : Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k distinct characters. If the given string doesn't have k distinct characters, return 0.
# https://leetcode.com/problems/subarrays-with-k-different-integers
#Python solution based on an easier problem LeetCode 1358
def find_substring(s, k):
    record = {}
    res = idx = cnt = 0
    removed = '#'
    for i in range(len(s)):
        if s[i] != removed:
            cnt = 0
        record[s[i]] = record.get(s[i], 0) + 1 # if s[i] not in record, set it to 1
        if len(record) == k:   #k distinct letters
            while len(record) == k:
                record[s[idx]] -= 1    #idx: idx of the first letter of the substring
                if record[s[idx]] == 0: #remove the first letter of the substring
                    removed = s[idx]
                    del record[s[idx]]
                idx += 1                #shift by one move to the next k letter. 
                cnt += 1
            res += cnt    # cnt is 1, 2,3,1 =>total=7
    return res


def test_driver(s,k, result):
    ret = find_substring(s, k)
    print(s,k,result)
    print("resut :", ret)
    print("expected: ",result, end="\n\n")
    assert ret==result
test_driver("pqpqs", 2, 7) #Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
test_driver("aabab", 3,0)

