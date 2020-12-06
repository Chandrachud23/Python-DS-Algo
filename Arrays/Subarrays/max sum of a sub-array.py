To find the maximum sum of a contiguous subarray,i.e, in an array [-1,2,7,6], [2,76] is an contiguous subarray while [-1,2,6] is not!
Kadane's Algorithm
def max_subarray(a):
    max1=-99999999999999999999 #a relatively very small number
    sum1=0
    for i in range(len(a)):
        sum1 += a[i] #for storing sum of each contiguous sub-array
        if sum1 < 0:
            sum1 = 0
        max1=max(max1, sum1)
    return max1

a=[-2, -3, 4, -1, -2, 1, 5, -3]
max_subarray(a)
