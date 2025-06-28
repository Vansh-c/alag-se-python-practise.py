# here we will use newton method to find roots 


def f(x):
    return x*x - 2*x - 3 


def df(x):
    return 2*x - 2 



print("enter maxitr , and initial value ")
x0= float(input("enter intial value : "))
h = 0 ; 
x1 = 0 
itr = 0
maxitr = int(input("enter maximum iteration : "))


while(itr<maxitr):
    h = f(x0) / df(x0) 
    x1 = x0 - h 
    x0 = x1 
    itr += 1 


print(f"the  value after {itr} iterations is {x0}")
