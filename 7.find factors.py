# find factors of the numbers 

def factor(n):
    
    for i in range(1 , n):
        if(n%i == 0):
            print(i)



num = int(input("enter a number : "))

print('the factors of the numbers are :')
factor(num)