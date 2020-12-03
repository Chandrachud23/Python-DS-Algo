def InsertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while key < arr[j] and j >= 0: 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
     
    return arr
  
# Driver code to test above 
arr = [23,45,53,12,34,9,84] 
InsertionSort(arr)
