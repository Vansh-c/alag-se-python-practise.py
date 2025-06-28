# program to find a number 
l = []

while(True):
    ask = int(input('enter a number: '))
    if(ask == 0):
        break

    l.append(ask)



print(l)
length = len(l)

findnum = 3

for i in range(0,length):
    if(l[i] == findnum):
        print("the number exists at index " , i)
        break


    else:
        if(i == length-1):
            print("the number do not exists")
       











