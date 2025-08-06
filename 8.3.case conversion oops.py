# converstion from upper to lower and lower to upper using oops 


class conversion:
    def __init__(self, strg):
        self.strg = strg
        
        
    def convert(self):
        if(self.strg.isupper()):
            print("now given text is converted to lowercase") 
            print(self.strg.lower())
        else:
            print("now given string is converted into upper case") 
            print(self.strg.upper())
            
            
user = input("enter string : ") 
s = conversion(user) 
s.convert()