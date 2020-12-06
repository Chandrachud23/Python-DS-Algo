Problem:

Given an unsorted array A of size N of non-negative integers, find a continuoussubarray which adds to a given number S.

Constraints
1 <= N <= 10^5 #Therefore we need order of time complexity to be < n^2
0 <= Ai <= 10^10

Example
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4

Explanation: The sum of elements from 2nd position to 4th position is 12.

Slution:
a=[1,2,3,7,5] #initialising array for simplicity
sum=10 # entered the sum for simplicity

start = 0
curr_sum = a[0]

for i in range(1,len(a)): #O(n^2)
    
    #If curr_sum exceeds the sum, then remove the starting elements 
    while curr_sum > sum and start < i-1:
        curr_sum = curr_sum - a[start] 
        start += 1
    
    if curr_sum == sum:
        print("Sum found between {} and {}".format(start,i-1))
        break #if this condition satisfies, we just need to be ut of the loop!
    
    #add another element if above two conditions fail
    if i < len(a):
        curr_sum += a[i]
