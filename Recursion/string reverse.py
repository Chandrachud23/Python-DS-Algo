def reverse(str1):
    if len(str1)==0:
        return
    str2=str1[1:]
    reverse(str2)
    print(str1[0])
    
str1="github"
reverse(str1)
