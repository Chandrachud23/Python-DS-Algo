#octal to decimal
def OctalToDecimal(num): 
      
    decimal_value = 0 
    base = 1
  
    while (num): 
        last_digit = num % 10
        num = int(num / 10)
        decimal_value += last_digit * base
        base = base * 8  
    print("The decimal value is :",decimal_value)

OctalToDecimal(232)


#decimal to octal
def DecimalToOctal(num):
    
    decimal_value = int(num,8) #It takes only string values
    print("The decimal value of {} is {}".format(num,decimal_value)) 

num=232
DecimalToOctal(str(num))
