# here we will write an algorithm to sort an array 


def a(arr , l, new):
    for i in range(0,l):
        min = i 
        for j in range(0,l):
            if(arr[j]<arr[min]):
                min = j 

        if(min != i):
           tmp = arr[min] 
           arr[min] = arr[i] 
           arr[i] = tmp

        new.append(arr[i])


    print(new)


      

arr = [4,3,7,2,1]
new = []


a(arr, len(arr) , new)

