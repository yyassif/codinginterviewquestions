def maxSubarray(arr):
    n=len(arr)
    temp = maxsub=maxseq=arr[0]
    for i in range(1,n):
        temp = max(arr[i], temp+arr[i])
        maxseq = max(arr[i], maxseq, maxseq+arr[i])  #maxseq = max sequence sum. diff is to compare arr[i] with running sum, prev sum
        maxsub = max(maxsub,temp) #max sub = max subarray sum
    return maxsub, maxseq
