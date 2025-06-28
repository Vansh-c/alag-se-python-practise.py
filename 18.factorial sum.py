# here to find sum of factorials Ex nc1 + nc2 + nc3+ nc4 

def fact_sum(n , r):
    return fact(n) / fact(r) / fact(n-r)


def fact(j):
    f  = 1 
    for i in range(1,j+1):
        f = f*i 


    return f 


m = int(input("enter value of m : "))
n = int(input("enter value of n : "))
s = 0 
for i in range(0,m+1):
    s = s + fact_sum(n,i)


print(s)