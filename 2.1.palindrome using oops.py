import math 

class palindrome:
    def __init__(self, number):
        self.number = number 
        
    def checkpalindrome(self):
        orig_num = self.number 
        rev =  0 
        
        while(self.number!=0):
           rev = rev*10 + self.number%10 
           self.number = math.floor(self.number/10)      
           
        print(rev)  
        
        if(rev == orig_num):
            print("palindrome") 
            
        else:
            print("NOT AN PALINDROME")
        

# class for user input 

class enterNumber:
    def __init__(self,num):
        self.num = num 
        
    def enteredInput(self):
        print("enter the number ")
        user = int(input())
        self.num = user
        

number = 0 
n = enterNumber(number) 
n.enteredInput() 

# checking whether the number is palindrome or not 

p = palindrome(n.num) 
p.checkpalindrome()
        
    