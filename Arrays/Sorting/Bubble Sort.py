def array(arr):
    
    l=len(arr)
    for i in range(l):
        
        for j in range(l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
    return arr
            
arr=[23,45,53,12,34,9,84]
array(arr)
