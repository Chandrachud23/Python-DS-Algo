Problem-(Amazon, Oracle)
Given an array arr[] of size N. The task is to find the first repeating element in an array of integers, i.e., 
an element that occurs more than once and whose index offirst occurrence is smallest.

Example
Input:
7
1 5 3 4 3 5 6
Output:
2
Explanation:
5 is appearing twice and its first appearance is at index 2 which is less than 3
whose first occurring index is 3.

a=[0,-10,1,3,20,3,-1,1]
freq={}
for i in a:
    if i in freq: #calculating frequency of each number
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

for i in freq:
    if freq[i]>1:
        # Key index in Dictionary 
        ind = list(freq.keys()).index(i) #to find index of matching 
        break
  
# printing result  
print("Index of first repeating number in array is : " +str(ind))
