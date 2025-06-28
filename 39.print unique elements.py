# program to print the unique elements in an array 


numbers = [1,2,3,3,4,5,5]; 
words = []
l = len(numbers)



def unique(n , l):

    for i in range(0 , l):
        r = False
        
        m = n[i]
        for j in range(0 , l):
            if(m == n[j] and i!=j):
                r=  True 
                break
            
        if(r == False):
            print(m)

            

         


unique(numbers , l)
