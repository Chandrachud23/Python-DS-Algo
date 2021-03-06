Google Kickstart
Problem:
Isyana is given the number of visitors at her local theme park on N consecutive
days. The number of visitors on the i-th day is Vi.
A day is record breaking if it satisfies both of the following conditions:
● The number of visitors on the day is strictly larger than the number of visitors on each of the previous days.
● Either it is the last day, or the number of visitors on the day is strictly larger than the number of visitors on the following day.
Note that the very first day could be a record breaking day!


Solution:

def record_breaker(a):
    
    count = 0
    key = -9999999999999999 # a relatively very small number
    
    for i in range(len(a)):

        if a[i] > key and a[i] > a[i-1]:
            count+=1
            print(i,a[i]) #check description for answer
            
        key = max(key,a[i])

    return count

a=[23,45,53,12,34,9,84]
record_breaker(a)
