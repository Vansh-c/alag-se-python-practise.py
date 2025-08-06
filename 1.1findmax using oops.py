# this is function to find max 
class findmax:
    def __init__(self, numList):
        self.numList = numList
        self.max = 0 
        
        
    def maxinum(self):
        
        for number in self.numList:
            if(number > self.max):
                self.max = number 
                
    def printnum(self):
        print("the maximum number from list is " , self.max)
        
        
# below is to add elements inside list . 

class addElements:
    def __init__(self , lst):
        self.lst = lst
        
    def insertElements(self):
        print("enter the number to add to element")
        while(True):
            user = int(input())
            if(user < 0):
                break 
            
            self.lst.append(user)
        
        

print("enter the number below ") 
# adding elements to list
empty_list = []
new_list = addElements(empty_list) 
new_list.insertElements()


max_num = findmax(new_list.lst)
max_num.maxinum() 
max_num.printnum()
             
    