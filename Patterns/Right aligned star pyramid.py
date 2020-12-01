def mirror(n): 
      
    # total number of spaces(in 5=4+3+2+1=10=2n) 
    k = 2*n-2
  
    # outer loop to handle number of rows from 1 to n 
    for i in range(0, n): 
      
        # inner loop to handle number spaces 
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 2 #for k=k-1 we would get a normal pyramid) 
      
        # inner loop to handle number of columns  
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = 5
mirror(n)
