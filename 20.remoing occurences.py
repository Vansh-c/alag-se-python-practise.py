# here we write a program which removed all the occurence of  a given character 


def rem(str , lis , char):
    length = len(str) 
     
    for i in range(0 , length):
        if(str[i]!=char):
            lis.append(str[i])

    s = "".join(lis)
    print(s)



lis = []
str = "this is string" 
char = "i"

rem(str, lis , char)

     