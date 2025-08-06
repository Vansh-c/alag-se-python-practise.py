# fibonacci using oops 

# functiion to find fibonacci 

def fib(num):
    if(num == 0 or num == 1):
        return num 
    else:
        return fib(num-1) + fib(num-2)
    
    

class fibonacci:
    def __init__(self, num):
        self.num = num 
        
    def printSeries(self):
        for i in range(self.num):   
            print(f" {fib(i)}")
            
            
user_input = int(input("enter the number : "))
num1 = fibonacci(user_input) 
num1.printSeries()
