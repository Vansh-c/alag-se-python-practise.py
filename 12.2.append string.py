# appending string using oops. 

class appendString:
    def __init__(self , s1 , s2):
        self.s1 = s1 
        self.s2 = s2 
        self.s3 = []
        
        
    def append(self):
        l=  len(self.s1)
        for i in range(l):
            self.s3.append(self.s1[i])
            
        for j in range(len(self.s2)):
            self.s3.append(self.s2[j]) 
            
    def printmergedString(self):
        self.s3 = ''.join(self.s3)
        print(self.s3) 
        
        
s1 = input("enter string  1: ")
s2 = input("enter string  2: ")

sappend = appendString(s1, s2) 
sappend.append()
sappend.printmergedString()

