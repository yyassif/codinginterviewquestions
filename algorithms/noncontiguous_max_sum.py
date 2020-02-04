# non contiguous max sum
# reference http://blog.gainlo.co/index.php/2016/12/02/uber-interview-question-maximum-sum-non-adjacent-elements/
arr= [5, 1, 1, 5] 
sum =0
mem= [-1]*len(arr)
def find(i):
  global mem
  if i==0:
    return arr[0]
  if i==1:
    return max(arr[0], arr[1])
  if mem[i]!=-1:
    return mem[i]
  mem[i] = max(find(i-1), arr[i]+find(i-2))  #either choose arr[i-1] or sum arr[i] with find(i-2) for non contiguous max sum
  return mem[i]
ret = find(len(arr)-1)
print(ret)
