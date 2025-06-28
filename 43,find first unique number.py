# program to find first unique number 


s = "ansh arohnis "

l = len(s)

i = 0 

while(i<len(s)):
    m= s[i]
    accept= True

    for j in range(0, l):
        if(m == s[j] and i !=j ):
            accept = False 

            break 

    if(accept):
        print(s[i])
        break

    i+=1
            
