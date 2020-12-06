def max_circular_subarray(a):
    c=a+a #to concat array
    n=len(c)
    del c[n-1] #when a circular arrow is unfolded it runs from 0 to 2(len(a))-1
    #print(c)
    max1=-99999999999999999999 #a relatively very small number
    sum1=0
    for i in range(len(c)):
        sum1 += c[i]
        if sum1 < 0:
            sum1 = 0
        max1=max(max1, sum1)
    return max1

a=[8, -8, 9, -9, 10, -11, 12]
max_circular_subarray(a)
