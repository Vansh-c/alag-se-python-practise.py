# program to print first repeating character 


s = "this aaa"
l = len(s)

i = 0 

while(i<len(s)):
    m = s[i]
    repeat = False
    for j in range(0 , l):
               if(m == s[j] and i!=j and m!= " "):
                  repeat = True 
                  break


    if(repeat):
        print(s[i])
        break


    i+=1