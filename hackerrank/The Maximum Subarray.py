def maxSubarray(arr):
    m=[]
    current_max=global_max=max_sum=arr[0]
    for i in range(1,len(arr)):
        current_max=max(arr[i],current_max+arr[i])
        max_sum=max(max_sum,arr[i],arr[i]+max_sum)
        global_max=max(global_max,current_max)
    m.extend([global_max,max_sum])
    return m
