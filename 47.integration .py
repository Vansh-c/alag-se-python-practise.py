# trapezoidal integration 


def func(x):
    return x*x



print("enter limits a and b") ; 
a = int(input("enter  limit a: "))
b = int(input("enter limit b: "))
n = int(input("enter number of subintervales : "))

h = 0 
x = 0 
integration = 0 ; 
sum = 0 


if(b>a):
    h = (b-a)/n
    for i in range(0,n):
        x = a + i*h 
        sum = sum + func(x) 

    integration = (h/2)*(func(a) + func(b) + sum*2)

print(f"the integration is {integration}")


