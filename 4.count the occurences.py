# program to find the number of occurences 

l = []

while(True):
    ask = int(input('enter a number: '))
    if(ask == 0):
        break

    l.append(ask)


print(l)
length = len(l)
n  = int(input("which number you want to find: "))


def occurences(num, length):
    count = 0
    for i in range(0,length):
        if(l[i] == num):
            count = count + 1

    return count


f=  occurences(n , length)


print(f"the given number${ask} repeated {f} times")
    
    
