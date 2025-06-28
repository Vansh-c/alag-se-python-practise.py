# to check whether a given number is armstrong or not 
import math as m


def armstrong( n ):
    sum = 0 
    tmp = n

    while(n!=0):
        rem = n%10 
        sum = sum + rem**3 
        n = m.floor(n/10)

    print(sum)

    if(sum == tmp):
        return True 
    
    else:
        return False
    

n = int(input('enter a number : '))

if(armstrong(n)):
    print("given number is an armstrong number")

else:
    print("given number is not armstrong ")


    