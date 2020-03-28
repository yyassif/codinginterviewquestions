#efficient sol
def primality(n):
    if n == 1 :
        return 'Not prime'
    elif n in set({2,3,5})  :
        return 'Prime'
    elif n%2 == 0 or n%3==0 :
        return 'Not prime'
    i = 5
    count = 0
    while(i*i<=n):
        if(n%i == 0 or n%(i+2) == 0):
            return 'Not prime'
        count += 2
        i += 6
    print('Checks performed : ', count)
    return 'Prime'
    
 #sieve of Eratosthenes is not efficient way to solve this problem, as it finds all prime numbers between 2 and N
 def primality(n):
    arr = [False]*(n+1)
    arr[0]=True
    arr[1] = True
    for i in range(2, n//2+1):
        for j in range(i,n+1,i):
            arr[j] = True
    return "Prime" if arr[n]==False else "Not prime"
