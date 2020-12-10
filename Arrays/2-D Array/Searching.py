import numpy as np 
  
n1 = int(input("Enter the number of rows:"))
n2 = int(input("Enter the number of columns:")) 

print("Enter the entries 1 in a single line (separated by space): ")
e1 = list(map(int, input().split()))

m1 = np.array(e1).reshape(n1, n2)
y=int(input("Enter num to be searched"))

if True in map(lambda x: y in x, m1): #lamda x is like a short form of the a function x like- def find(x): and then the rest
    print("Found")
else:
    print("There is no {} in the given matrix".format(y))
