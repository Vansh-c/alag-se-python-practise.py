# here we will know about binary sort  . 
import math as m


def binary_sort(s , key):
    l = 0 
    r = len(s) 

    while(l+1!=r):

        mid = m.floor((l+r)/2)
        
        if(s[mid]<key):
            l = mid

        else:
            r = mid


    print("value of given key lies at" , r)
        



a= [1,2,3,4,5,6]

binary_sort(a , 5)

        

