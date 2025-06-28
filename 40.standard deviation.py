# program to compute standard deviation 
import math as m



num = [2,3,4 , 5]
l = len(num)


def std_dev(n , l):
    mean = 0 
    total = 0 

    for i in range(0 , l):
        total = total + n[i] ; 

    mean = total / l 

    sum = 0 
    for i in range(0 , l):
        sum = sum + (n[i] - mean)**2 


    deviation = sum 

    return m.sqrt(deviation)


print("the standard deviation is " , std_dev(num , l))
