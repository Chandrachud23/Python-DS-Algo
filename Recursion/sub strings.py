def lst_substrings(s,ans):
    if len(s) == 0:
        print(ans)
        return
    ch=s[0]
    ros=s[1:]
    
    lst_substrings(ros,ans)
    lst_substrings(ros,ans+ch)

s="ABC"
ans=""
lst_substrings(s,ans)

#Watch this for better explanation: https://www.youtube.com/embed/j9RG18jfnRY?list=PLfqMhTWNBTe0b2nM6JHVCnAkhQRGiZMSJ
