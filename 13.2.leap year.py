# leap year using oops 

class checkleapyear:
    def __init__(self, year):
        self.year = year 
        
    def check(self):
        if(self.year%4!=0):
            return False 
        elif(self.year%100==0 and self.year%400!=0):
            return False ; 
        else:
            return True 
        
    def checkFalse(self):
        print(f'{self.year}') 
        
    def checkTrue(self):
        print(f'{self.year} leap year') 
        
        
    
for i in range(1900  , 2100):
    if(checkleapyear(i).check()):
        checkleapyear(i).checkTrue() 
    else:
        checkleapyear(i).checkFalse()
    