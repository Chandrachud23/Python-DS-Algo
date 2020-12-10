import numpy as np 
  
n1 = int(input("Enter the number of rows of matrix 1:")) 
n2 = int(input("Enter the number of rows of matrix 2 which will be same as columns of matrix 1:")) 
n3 = int(input("Enter the number of columns of matrix 2:")) 

print("Enter the entries 1 in a single line (separated by space): ")
e1 = list(map(int, input().split()))
print("Enter the entries 2 in a single line (separated by space): ")
e2 = list(map(int, input().split()))
    
# For printing the matrix 
m1 = np.array(e1).reshape(n1, n2) #shapping the data into an array of size n1 x n2
m2 = np.array(e2).reshape(n2, n3)
m3 = np.zeros((n1,n3)) #to fill with zeros of order n1 x n3

m3=np.dot(m1,m2) #vector like multiplication using numpy

for r in m3: 
    print(' '.join(map(str,r))) #to remove the array parentheses 
