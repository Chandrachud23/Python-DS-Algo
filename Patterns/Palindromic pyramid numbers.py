def pallin(n): 
      
    # outer loop to handle number of rows 
    for i in range(1,n+1): 

        for j in range(1,n-i+1): 
            print(end="  ")
      
        k=i+1
        # inner loop to handle number of columns 
        for j in range(n-i+1,n+1): 
            # printing stars 
            k=k-1
            print(k,end=" ")
            
        k=1
        for j in range(n+1,n+i):
            k=k+1
            print(k, end=" ")
      
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = 5
pallin(n)


#if we want an left aligned sequence(without a equilateral triangle

#we will use the mathematical trick
#11*11=121
#111*111=12321 ans so on
def series(n):
   
    for i in range(1, n+1):
        print((111111111//(10**(9-i)))**2, end=" ") #the floor division // rounds the result down to the nearest whole number

        print("\r")
        
n=5
series(n)
