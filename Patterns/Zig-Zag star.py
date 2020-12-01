def zigzag(n):
    
    for i in range(1,4): #It has only 3 rows
        for j in range(1,n+1):
        #i and j stand for rows and columns, if you look at description and allot them in the form of matrix, you will have the following observation that the addition of i an j of many are multiples of 4 except the ones adding to 6,10 and so on but that also has a fixed value of i=2 and j is a multiple of 4.
            if((i+j)%4==0) or ((i==2) and (j%4==0)):
              print("*",end=" ")
            else:
              print(end= "  ")
            
        print("\r")
n=9
zigzag(n)
