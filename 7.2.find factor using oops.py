# to find factors of a number using oops 

def f(n):
    for i in range(1, n+1):
        if(n%i==0):
            print(i , end=' ')


class factor:
    def __init__(self, n):
        self.n = n 
        
    def factorofnumber(self):
        f(self.n) 
        
        
        
num = int(input("enter the number: ")) 
r = factor(num) 
r.factorofnumber()