# here we will see how to add vectors 

def vector_add(v1 , v2 , v3):
    for i in range(0 , len(v1)):
        v3.append(v1[i] + v2[i])


v1 = []
for i in range(0,3):
    ask = int(input(f"v[{i}]: "))
    v1.append(ask)
print("the first vector is ", v1)


v2 = []
for i in range(0,3):
    a = int(input(f'v2[{i}]'))
    v2.append(a)
print("the second vector: ", v2)



v3 = []

vector_add(v1 , v2 , v3)

print(v3)