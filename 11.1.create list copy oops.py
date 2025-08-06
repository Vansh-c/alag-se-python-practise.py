# // creating  list copy using oops 
class listcopy:
    def __init__(self,l1):
        self.l1 = l1
        self.l2 = [] 
        
    def inputlist(self):
        print("enter the elements  of array ")
        while True:
            try:
                user = int(input())
                self.l1.append(user)
            except ValueError:
                print("You entered keyboard input non integer")
                break
                
    def copy_array(self):
        for i in range(len(self.l1)):
            self.l2.append(self.l1[i])
            
    def print_array(self):
        
        print(self.l2) 
        
l1  = []
new_arr = listcopy(l1) 
new_arr.inputlist()
new_arr.copy_array()
new_arr.print_array()

