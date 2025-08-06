
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
        

print("enter the number below ") 
list = [1,2,4,5 , 67] 
max_num = findmax(list)
max_num.maxinum() 
max_num.printnum()
             
    