def binary_search(arr, n, key):
    arr.sort() #buit-in func
    if key==arr[n//2]: #// is a flooring operation, rounds up value to a whole num, instead can declare it as int and continue with normal division operator
        return n//2
    elif key<n//2:
        for i in range(0, n//2):
            if (arr[i] == key):
                return i
    elif key>n//2:
        for i in range(n//2,n):
            if (arr[i] == key):
                return i 
    else:
        return 0
 
 
# Driver Code
arr = [5, 10, 15, 20, 21, 23, 43, 54]
key = 23
n = len(arr)
 
# Function call
result = binary_search(arr, n, key)
if(result == 0):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
