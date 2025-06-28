# a program to convert from binary to decimal 

def bin_to_dec( n):
    total = 0 
    decimal = 1 
    l = len(n)

    for i in range(l-1 , 0 , -1):
        if(n[i] =='1'):
           total = total + decimal
        
        decimal = decimal*2


    return total 


s = "0111"

print(bin_to_dec(s))

    
