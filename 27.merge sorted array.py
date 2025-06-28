# here we will write a program to merge sorted array 


def merge(a1 , a2 , l1 , l2 , a3):
    i  = 0 
    j = 0 
    

    while(i<l1 and j<l2):
        if(a1[i]<a2[j]):
            a3.append(a1[i])
            i = i+1 

        else:
            a3.append(a2[j])
            j+=1


    while(i<l1):
        a3.append(a1[i])
        i+=1

    while(j<l2):
        a3.append(a2[j])
        j+=1


a1 = [1,7,3,4,5] 
a2= [6,2,8,9,10] 
l1 = len(a1) 
l2 = len(a2 )
a3 = []

merge(a1 , a2 , l1 , l2 , a3) 

print(a3)