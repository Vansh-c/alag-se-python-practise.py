#  program to find minimum occuring character 


def min_occuring(s , l):
    min_char = ' '
    unique = []
    counted = 0 
    min_counted = 0 


    for i in range(0 ,l):
        repeat = False 
        m = s[i]
        for j in range(0,len(unique)):
            if(m == s[j]):
                repeat = True

        if(repeat):
            continue 

        if(m == ' '):
            continue

        count = 0 

        for j in range(0 , l):
            if(m == s[j] and m!= ' '):
                count+=1


        counted = counted + 1 



        if(counted == 1):
            min_char = s[i]
            min_counted = count


        if(count<min_counted):
            min_char = s[i] 
            min_counted = count 

        unique.append(s[i]) 


    print(f"the minimum character is {min_char} which occurred {min_counted} itmes")


str = "the black getsuga jujisho" 

l = len(str) 

min_occuring(str , l)
