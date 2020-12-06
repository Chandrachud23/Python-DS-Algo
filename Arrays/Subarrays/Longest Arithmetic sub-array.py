Google kickstart
Problem Statement:

An arithmetic array is an array that contains at least two integers and the differences between consecutive integers are equal.
For example, [9, 10], [3, 3, 3], and [9, 7, 5, 3] are arithmetic arrays, while [1, 3, 3, 7], [2, 1, 2], and [1, 2, 4] arenot arithmetic arrays.
Saraswati has an array of N non-negative integers. The i-th integer of the array is Ai.
She wants to choose a contiguous arithmetic subarray from her array that hasthe maximum length. Help her to determine the length of the longest continuous arithmetic subarray.

Solution:

array = [int(a) for a in input("Enter numbers to find largest arithmetical sub-array").split()]

diff = array[1] - array[0]
curr_arth_array = 2 #current arithmetic array

for i in range(2, len(array)):
    
    if (array[i] - array[i-1]) == diff:
        curr_arth_array += 1
    
    else:
        diff = array[i] - array[i-1]
        curr_arth_array = 2
    
    ans = max(2,curr_arth_array)

print(" Largest arithmetic array is",ans)
