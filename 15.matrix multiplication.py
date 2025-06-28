# a program to do matrix multiplication 


mat1 = [[0,0], [0,0]]
mat2 = [[0,0] , [0,0]]


print("enter matrix 1")

for i in range(0,2):
    for j in range(0,2):
        mat1[i][j] = int(input(f" mat1[{i}][{j}] = "))

print()

for i in range(0,2):
    for j in range(0,2):
        print(mat1[i][j] , end=' ')

    print()


print("enter matrix 2")


for i in range(0,2):
    for j in range(0,2):
        mat2[i][j] = int(input(f" mat2[{i}][{j}] = "))

print()


for i in range(0,2):
    for j in range(0,2):
        print(mat2[i][j] , end=' ')

    print()


print()

sum = [[0,0] , [0,0]]
for i in range(0, 2):
    for j in range(0 , 2):
        for k in range(0,2):
            sum[i][j] = sum[i][j]+ mat1[i][k]*mat2[k][j]
    print()


for i in range(0,2):
    for j in range(0,2):
        print(sum[i][j] , end=' ')

    print()

