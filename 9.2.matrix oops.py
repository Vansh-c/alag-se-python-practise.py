# making matrix usinig oops 



class matrix_maker:
    def __init__(self, list , a,  b) :
        self.list = list 
        self.a = a 
        self.b = b
        
        
    def matrix_addelements(self):
        print("enter matrix  elements ")
        for i in range(self.a* self.b):
                user = int(input())
                self.list.append(user)
                
    def print_matrix(self):
        for i in range(self.a):
          for j in range(self.b):
              print(self.list[i*self.b +j] , end=' ')
          print()   
              
            
            
emptyList= []
matA = matrix_maker(emptyList , 2,2)
matA.matrix_addelements()
print()
matA.print_matrix()
        