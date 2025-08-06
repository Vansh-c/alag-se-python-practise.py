# here we will count the occurence of a specific elements using oops.

# making of a user input function 

class new_list:
    def __init__(self):
        self.l = [] 
        
    def add_elements(self):
        print("enter the eleements :") 
        while(True):
            try:
                user = int(input()) 
                self.l.append(user)
            except (ValueError):
                break 
            
    def printElements(self):
        print(self.l)
            
            
# well let's try inheritance 

class count_occ (new_list):
    def __init__(self , num, data_list):
        super().__init__()    # calling of chlid class constructor.
        self.num = num 
        self.l = data_list
        
        
    def count_occurences(self):
        count = 0 
        for i in range(len(self.l)):
            if(self.l[i] == self.num):
                count = count + 1
                
        print(f"number {self.num} occured {count} times")
        
        
a_list = new_list() 
a_list.add_elements()
a_list.printElements() 


# taking user input to find the occrences 

user = int(input("enter the number for which you want to find occurecnes: ")) 
occ= count_occ(user, a_list.l)
occ.count_occurences()