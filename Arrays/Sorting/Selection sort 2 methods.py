#Using normal method of finding min num first
def array(arr):
    
    for i in range(len(arr)):
        min=i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min=j
        arr[i], arr[min] = arr[min], arr[i]
    return arr
            
arr=[23,45,54,12,34,9,84]
array(arr)


#But Python developers had diff plans-
#They laid out a built-in function
arr.sort() #LOL
