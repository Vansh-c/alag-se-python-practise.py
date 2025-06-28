# in this program we will write binary search algorithm 


def binary_search(a , l):
    i =  0
    j =  0
    for i in range(0 , len(a)):
        for j in range(0 , len(a)-i-1):
             if(a[j] > a[j+1]):
                 tmp1 = a[j]
                 tmp2 = a[j+1]
                 a[j+1] = tmp1
                 a[j] = tmp2

    
            
    return a 


a = [2,3,1,5,4] 
l = [] 

print("before: ", a)
print("after :" , binary_search(a,l))
