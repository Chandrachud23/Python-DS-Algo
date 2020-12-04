Problem- (Amazon, Samsung, Snapdeal, Accolite)
Find the smallest positive number in the given array.
Example: [0, -10, 1, 3, -20], Ans = 2


Solution:
a=[0,-10,1,3,20] #one can also input their array

for i in range(len(a)):
    if a[i]<0: #the -ve terms we are updating as 0
        a[i]=0
key=9999999999999999999 #just a large positive number

for i in range(len(a)):
    if a[i]>0: #findin
        key=min(key,a[i])

for i in range(len(a)):   
    if a[i]==key:
        print("Element is present at index",i)  
