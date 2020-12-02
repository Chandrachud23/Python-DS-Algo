import math

def nCr(n,r):
        ans= fact(n)/(fact(r)*fact(n-r))
        print(ans)

def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial
    
nCr(5,3)
