def solution(N):
    # write your code in Python 3.6
    cnt =0 #cnt zeroes between 1's
    maxi=0    
    #skip rightmost zeroes
    while N&1 !=1:
        N = N>>1
        
    #skip ones
    while N!=0:
        while N&1 ==1:
            N = N>>1
        cnt=0
        while N!=0 and N&1 ==0:
            N = N>>1
            cnt += 1
        maxi = max(maxi, cnt)
    return maxi
