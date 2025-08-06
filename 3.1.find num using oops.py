# a program to demonstrate finding of a number by using oops.

# function to check elements 

def check_num(user_input , l):
    for i in range(len(l)):
        if(l[i] == user_input):
            print("number exist at index = " , i  )
            return 
    print("not found")
            


# making of a list by user input 

class user_list:
    def __init__(self):
        self.l = []
        
        
    def listElements(self):
        print("enter the elements of  the list\n") 
     
        while(True):
            try:
                   user = int(input()) 
                   self.l.append(user) 
            except ValueError:
                break
            
        
    def printList(self):
        print(self.l) 
        
        
        
        
a_list = user_list()
a_list.listElements() 
# a_list.printList()

# checking whether the number  is found of not . 

user_inp = int(input('enter the element you want to search : '))
check_num(user_inp , a_list.l)