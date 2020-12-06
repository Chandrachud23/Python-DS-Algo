def pair_sum(a,k): #a=array,k=reqd sum of the array
    a.sort() #sorting the array is of utmost importance
    n=len(a)
    start=a[0]
    end=a[n-1]
    for i in range(n):
        if start+end < k:
            start = a[i]
        elif start+end > k:
            end = a[i]
        else:
            return end,start
a=[-2, -3, -4, -1, -2, -1, -5, -3]
k=-6
pair_sum(a,k)
