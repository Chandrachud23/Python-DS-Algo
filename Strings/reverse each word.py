string="Hello world I am Gugul"
lst=[]
lst1=[]
for i in range(len(string)):
    if string[i] != " ":
        lst.append(string[i])
    if string[i] ==" " or i==len(string)-1:
        lst1.append(lst[::-1])
        lst=[]
    
#pint lst1 would yield this[['o', 'l', 'l', 'e', 'H'], ['d', 'l', 'r', 'o', 'w', ' '], ['I', ' '], ['m', 'a', ' '], ['l', 'u', 'g', 'u', 'G', ' ']]
print(" ".join(list(map(''.join, lst1)))) #for removing parenthesis we used list and map and then to join the inner braces wala elements and separating them with spaces introduced 2nd jin
