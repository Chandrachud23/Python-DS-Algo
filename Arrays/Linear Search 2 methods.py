# Method 1
def linear_search(arr, n, key):
 
    for i in range(0, n):
        if (arr[i] == key):
            return i
    return 0
 
 
# Driver Code
arr = [67, 53, 43, 23, 85]
key = 23
n = len(arr)
 
# Function call
result = linear_search(arr, n, key)
if(result == 0):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
    
    
# Method 2
key=int(input("Enter key"))
arr = [int(item) for item in input("Enter the list items for num: ").split()] 
for i in range(len(arr)):
    if arr[i]==key:
        print("Element is present at index",i)
    else:
        print("Not in the array")
