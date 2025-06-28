l = []

while(True):
    ask = int(input("enter the number: "))
    if(ask<0):
        break

    l.append(ask)


max = l[0]
length = len(l)

for i in range (0,length):
    if(l[i]>max):
        max = l[i]


print("the maximum number among entered numbers is " , max)