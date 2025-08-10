# matrix multiplication using oops 

class matrixmultiply:
    def __init__(self, mata , matb ):
        self.mata = mata 
        self.matb = matb
        self.matc = makeMatrix(mata.rows , matb.cols)
   
        
    def multiply(self):
        for i in range(self.mata.rows):
            for j in range(self.matb.cols):
                c =  0 
                for k in range(self.mata.cols):
                  c = c + self.mata.mat[i*self.mata.rows + k]*self.matb.mat[k*self.matb.cols + j]
                self.matc.mat.append(c) 
                
    def printmat(self):
        self.matc.printMat()
        
    
        
        
        
        
class makeMatrix:
    def __init__(self , rows , cols):
        self.mat =  [] 
        self.rows = rows 
        self.cols = cols
        
        
    def enterElements(self):
        print("enter elements of array")
        for i in range(self.rows*self.cols):
            user = int(input())
            self.mat.append(user) 
            
            
    def printMat(self):
        print()
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.mat[self.rows*i + j] , end = ' ')
                
            print() 
            
print("enter row and columns") 
row = int(input('enter row : ')) 
cols = int(input("enter cols : ")) 

mata = makeMatrix(row , cols) 
mata.enterElements() 
mata.printMat()

print() 

matb = makeMatrix(row , cols)
matb.enterElements() 
matb.printMat() 

print() 

newmat = matrixmultiply(mata , matb ) 
newmat.multiply()
newmat.printmat()