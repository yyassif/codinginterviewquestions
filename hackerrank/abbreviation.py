#simpler sol
def abbreviation(a, b):
    m, n = len(a), len(b)
    dp = [[False]*(m+1) for _ in range(n+1)] #create (n+1) by (m+1) table of truth values. cols are vals of a rows are b
    dp[0][0] = True
    for i in range(n+1): # length of b
        for j in range(1,m+1): #length of a
            if a[j-1] == b[i-1]: #if already upper and value equals, get truth val from upper-left
                dp[i][j] = dp[i-1][j-1]
            elif a[j-1].upper() == b[i-1]: #if lowercase, check if matches as upper, 
                dp[i][j] = dp[i-1][j-1] or dp[i][j-1] #check if either left or upper-left is true
            elif a[j-1].islower():
                dp[i][j] = dp[i][j-1]   #if lower match with what's left
    return "YES" if dp[n][m] else "NO"

