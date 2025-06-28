# using insertion sort 


a = [4,3,1,7,2]  
l = len(a) 

for i in range(1 , l):
    key = a[i] 
    j = i-1 
    while(j>=0 and a[j]>key):
        t1 = a[j] 
        a[j+1] = t1 
        j = j -1

    a[j+1]  = key


print(a)