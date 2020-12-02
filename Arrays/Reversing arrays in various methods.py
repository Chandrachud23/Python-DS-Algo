# Using While method 
# Function to reverse A[] from start to end
def arrayreverse(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start] #no need for any temp variable used in C and Java
        start += 1
        end -= 1
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
arrayreverse(A, 0, 5)
print("Reversed list is")
print(A)


# Using the power of List
def arrayreverse(A):
  print( A[len(A)::-1]) #list[<start>:<stop>:<step>]
     
# Driver function to test above function 
A = [i for i in range(1,100)] 
print(A) 
print("Reversed list is") 
arrayreverse(A)
