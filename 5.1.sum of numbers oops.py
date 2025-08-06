# using oops to find sum of numbers 
# we will here again try inheritance to do  it 

# first we will do list input 

class array_elements:
    def __init__(self):
        self.l = [] 
        
    def addElemnts(self):
        print("enter the elements of array \n") 
        while(True):
            try:
                user = int(input())
                self.l.append(user) 
                
            except(ValueError):
                break 
            
    def printarray(self):
        print(self.l) 
        
# using inheritance

class add_array (array_elements):
    def __init__(self , arr):
        super().__init__() 
        self.arr = arr 
        
    def adding_elements(self):
        sum = 0 
        for elements in self.arr:\
            sum = sum + elements 
            
        print(f"summation of elements = {sum}")
        
        
new_arr = array_elements()
new_arr.addElemnts()
new_arr.printarray()

summation_arr = add_array(new_arr.l) 
summation_arr.adding_elements()



            
            
    
        