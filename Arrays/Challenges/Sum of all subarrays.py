Question:
Given an array a[] of size n. Output sum of each subarray of the given array.

Solution:
a=[1,2,2]

for i in range(len(a)):
    sum = 0
    
    for j in range(i,len(a)):
        sum += a[j]
        print(a[i:j+1],sum)
