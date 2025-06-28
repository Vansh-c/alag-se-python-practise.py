 # here we will write a progam so that we can remove the vowel from an array 

def remove(str , len  , lst):
    for i in range(0,len):
        if(str[i]=='a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u'):
            lst.append(' ')

        else:
            lst.append(str[i])

    return ''.join(lst)    


lst = [] 
str = input("enter string: ")
l = len(str) 

print("new array is : "  , remove(str , l , lst))
