def DecimalToOctal(decimal):
    
    octal = 0
    i = 1
    while (decimal != 0):
        o#Usingctal = octal + (decimal % 8) * i
        decimal = int(decimal / 8)
        i = i * 10
    return octal

DecimalToOctal(154)


def dec(decimal_num):
    octal_num = oct(decimal_num).replace("0o", "") # hex: 0x232;  oct: 0o232;  bin: 0b101010' Therefore the prefixes needs to be removed
    print("The octal value for {} is {}".format(decimal_num,octal_num))

dec(154)
