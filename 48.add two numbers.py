


def twoSum(l1 , target , l):
    store = [] 

    for i in range(l):
        for j in range(i+1 , l):
            if((l1[i] + l1[j]) == target):
                store.append(i) 
                store.append(j)
                 
                return store 
            

n  = int(input("enter value of n"))
i = 0 
l = []

while(i<n):
    e = int(input(f"l[{i}] = "))
    l.append(e) 
    i = i+1


print(l) ; 
print()
target = int(input("enter target value "))


rtrn = twoSum(l , target , n)

print(rtrn[0] , rtrn[1])

        