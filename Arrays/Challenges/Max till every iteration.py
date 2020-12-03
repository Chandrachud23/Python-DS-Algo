def max_in_everyI(a):
    
    key=-99999999999999999 #just entering a large negative number
    for i in range(len(a)):
        key=max(key,a[i])
        print("Till {}, {} is highest".format(i,key)) #.format is used to insert
    return

a=[23,45,53,12,74,9,84]
max_in_everyI(a)
