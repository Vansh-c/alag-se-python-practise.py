# to make fibonacci series without using recursions 

term1 = 0 
term2 = 1
fib = 0 

length = int(input("enter the number : "))


print(term1)
print(term2)
for i in range(0,length):
    fib = term1+ term2
    term1 = term2 
    term2 = fib 

    print(fib)


    