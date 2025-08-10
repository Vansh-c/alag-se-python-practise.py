# vector addtion by object oreinted programming 
# here we have used composition 



class vectors:
    def __init__(self , v):
        self.v = v
        
    def userinput(self):
        print("enter the elements of an vector")
        for i in range(3):
            user = int(input())
            self.v.append(user)
            
    def printvector(self):
        print(self.v)
        
        
class add_vectors:

    
    
    def __init__(self, v1 , v2 ):
        self.v1  = v1 
        self.v2 = v2 
        self.v3 = []
        
    
    def add(self):
        for i in range(3):
            self.v3.append(self.v1[i]+ self.v2[i])
            
        print(self.v3)
           
        
        
v1 = []
v2 = [] 
vectors(v1).userinput()
vectors(v2).userinput()

print(v1) 
print(v2)

add_vectors(v1,v2).add()
        
    