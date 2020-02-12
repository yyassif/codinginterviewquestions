#max min problem from hackerank
#sol from https://www.hackerrank.com/challenges/angry-children/forum
def maxMin(k, arr):
        ans = 10**9
        arr_s = sorted(arr)
        for i in range(len(arr) - k + 1):
                sub_arr_min = arr_s[i]
                sub_arr_max = arr_s[i+k-1]
                ans = min(sub_arr_max - sub_arr_min, ans)
        return ans
