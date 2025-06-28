# here we will write a program to convert from decimal to binary 
import math as m
def convert(n , l):

    length = 0 
    d = "0" 
    o = "1"

    for length in range(0 , 9):
        if(n%2 == 0):
            l.append(d)

        else:
            l.append(o)
            
        if(n == 0):
            break 

        length = length + 1 
        n = m.floor(n/2)


    p = "".join(l)
    return p[ : : -1]



l = [] 
n = int(input("enter value of n: "))

print(convert(n , l))


