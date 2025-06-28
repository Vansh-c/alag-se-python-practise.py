# using bissection method to find roots of a polynomial 



def func(x):
    return x*x - 2*x - 3


def bissection( a , b ):
    return (a+b)/2
    



print("enter intial limit , other limit  , allowed error and max iteration \n")

a = float(input("enter 1st number : "))
b = float(input("enter 2nd number: "))
allerr = float(input("enter allowed error: "))
maxitr = int(input("enter max interation: "))
itr = 0 
x = (a+b)/2
x1 = 0

while(itr<=maxitr):

    if(func(a)*func(x)<0):
        b = x 

    else:
        a = x 

    x1 = bissection( a , b  ) 

    if(((x1 - x)<allerr or -(x1-x)<allerr)  and itr == maxitr ):
        print("the roots after",itr , " iterations is " ,  x1)
        


    x = x1 
    itr = itr+ 1

