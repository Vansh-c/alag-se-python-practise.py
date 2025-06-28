# here we will make copy of list

l1 = [1,2,3]
l2 = []
len1 = len(l1)


def lcopy(l1 , l2 , len1):
    for i in range(0,len1):
        l2.append(l1[i])

lcopy(l1 , l2 , len1)

print(l2)
    
