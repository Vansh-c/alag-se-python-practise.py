# to find sum of all elements in an array and their average 

l = []

while(True):
    ask = int(input('enter a number: '))
    if(ask <0):
        break

    l.append(ask)


print(l)
length = len(l)

def summation(length):
    sum = 0
    for i in range(0,length):
        sum = sum + l[i]


    return sum


print("the sum of all the elements is ", summation(length))