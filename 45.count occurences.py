# a program to find occurences of eachh character in a strin 


def occurences(s , l):
    unique = []
    for i in range(0 , l):
        m = s[i] 
        repeat = False

        for j in range(0 , len(unique)):
            if(m == unique[j]):
                repeat  = True 
                break 


        if(repeat):
            continue

        count = 0 

        for j in range(0 , l):
            if(m == s[j] and m!=' '):
                count = count + 1


        if(m!=' '):
            print(f'{m} occured {count} times')
        unique.append(s[i])
        



    
str = "vansh v" 
l = len(str) 

occurences(str , l)







