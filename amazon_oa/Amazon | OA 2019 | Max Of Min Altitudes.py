#from https://leetcode.com/discuss/interview-question/383669/
#dynamic programming O(M*N) sol
def max_min_path(matrix):
    if not matrix or not matrix[0]:
        return 0
    n, m = len(matrix), len(matrix[0])
    if n<=2 and m<=1 or n<=2 and m<=1:
        return 0
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif i == 1 and j == 0 or i == 0 and j == 1:
                dp[i][j] = matrix[i][j]
            elif i == 0:
                dp[i][j] = min(matrix[i][j], matrix[i][j - 1])
            elif j == 0:
                dp[i][j] = min(matrix[i][j], matrix[i - 1][j])
            else: #check entries toward the center, not the edge cases
                dp[i][j] = min(matrix[i][j], max(dp[i - 1][j], dp[i][j - 1]))

    if n == 1:
        return dp[0][-2]
    elif m == 1:
        return dp[-2][0]
    else:
        return max(dp[-2][-1], dp[-1][-2])

def test_driver(data, result):
    print(data)
    print("expected: ", result)
    res = max_min_path(data)
    print("result: ", res)
    print(res)
    assert res==result


test_driver([[5, 1], [4, 5]], 4)
test_driver([[1, 2, 3],[4, 5, 1]], 4)
test_driver([], 0)
test_driver([[3]], 0)
