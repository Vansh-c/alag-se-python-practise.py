# a program to count unique elements in an array 

def c_uelets(a):
    count = 0 

    i = 0 
    j = 0 
    for i in range(0 , len(a)):
        for j in range(0 , len(a)):
           if(a[i] == a[j] and i!=j):
              break 
           j= j+1

        if(j == len(a)):
           count = count + 1


    return count 


arr = [1,2,2,3,4,4]

print("number of unique elements = " , c_uelets(arr))


    
        