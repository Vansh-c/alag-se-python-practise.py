# this is how to print matrix 


matrix = [[1,2,3] , [4,5,6] , [7,8,9]]

length = len(matrix)

for i in range(0 , length):
    for j in range(0 , len(matrix[i])):
        print(matrix[i][j] , end=' ')

    print()