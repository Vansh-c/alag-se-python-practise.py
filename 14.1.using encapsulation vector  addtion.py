# vector addtion by object oreinted programming 
# here we have used composition 



class vectors:
    def __init__(self):
        self.v = []
        
    def userinput(self):
        print("enter the elements of an vector")
        for i in range(3):
            user = int(input())
            self.v.append(user)
            
    def get_vector(self):
        return self.v
            
    def printvector(self):
        print(self.v)
        
        
class add_vectors:

    
    
    def __init__(self, v1 , v2 ):
        self.v1  = v1
        self.v2 = v2 
        self.v3 = []
        
    
    def add(self):
        for i in range(3):
            v1 = self.v1.get_vector()
            v2 = self.v2.get_vector()
            self.v3.append(v1[i]+ v2[i])
            
        print(self.v3)
           
        
        
v1 = vectors()
v1.userinput()
v2 = vectors()
v2.userinput()


add_vectors(v1,v2).add()
        
    