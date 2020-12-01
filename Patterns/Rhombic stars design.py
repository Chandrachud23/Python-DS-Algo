def rhombous(n): 
      
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # inner loop to handle number spaces 
        for j in range(0, n-i):
            print(end=" ") 
   
        # inner loop to handle number of columns 
        for k in range(0, n+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = 5
triangle(n)
