# here we will use selection sort 

def select(a  , k , len):
    pos = k 
    for j in range(k+1,len):    # here k+1 is written because once we have resolved the place issue of elements , 
        if(a[j]<a[pos]):
            pos = j 

    return pos


def selsort(a , len):
    for i in range(0,len):
          m = select(a , i , len)
          tmp1 = a[m] 
          tmp2 = a[i]
          a[i] = tmp1
          a[m] = tmp2
    

    return a


array = [5,12,-5 , 6 ,14 , 31, -17 ,46]

print(selsort(array , len(array)))