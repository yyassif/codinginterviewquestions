#Myungho Sim
#count and say problem from leetcode - work in progress
def countAndSay(n: int) -> str:
  ret="1"
  if n==1:
      return ret
  for i in range(n-1):
      digit=""
      string = ret
      size = len(string)
      cnt=0
      prev=""
      for j in range(size):
        ret =
          digit = string[j]
          if(prev==digit):
              cnt+=1
              if (j==size-1):
                  ret=str(cnt)+prev +
          elif (prev!=digit): #change in digit or reached the end
              if (j==size-1):
                  ret+=str(cnt)+digit
                  print("#",ret)
              else:
                  ret+=str(cnt)+prev
                  cnt=1
          prev = string[j]
  return ret
print(countAndSay(2))
