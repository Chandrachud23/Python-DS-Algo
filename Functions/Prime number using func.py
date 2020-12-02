import math #for sqrt func

def isPrime(n):
    for i in range(2,(int)(math.sqrt(n))+1): #sqrt will return a float type and will cause error
        if n%i == 0:
            return False
    return True

def main(a,b):
    for i in range(a,b):
        if isPrime(i):
            print(i)

main(5,15)
