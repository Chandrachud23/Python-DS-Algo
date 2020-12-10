lst=str(input()).split() #input a string and split where there is a blank space
res = max(lst, key = len)  #In this, we use inbuilt max() with “len” as key argument to extract the string with the maximum length.
print("Maximum length string is : ", res)
