# to find dot product between two vectors . 

def dot_product(v1 , v2 ,v3):
    for i in range(0 , 3):
        v3.append(v1[i] * v2[i])


print("enter first vector \n")

v1 = []
for i in range(0,3):
    l = int(input("enter number : "))
    v1.append(l)

print("\n enter second vector \n")


v2 = []
for i in range(0,3):
    l1 = int(input("enter number : "))
    v2.append(l1)


v3 = []

dot_product(v1 , v2, v3)

print("dot product of v1 and v2 is \n" , v3)
