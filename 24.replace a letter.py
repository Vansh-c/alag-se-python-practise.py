# here we will write a program to replace a letter 

def rep(f_str , r_str , l , replaceword , chooseword):
    for i in range(0,l):
        if(f_str[i] == chooseword):
              r_str.append(replaceword)
             

        else:
            r_str.append(f_str[i])



    p = "".join(final_string)
    print(p)


final_string = [] 
str = "The black getsuga tenshou "
lee = len(str)
replaceword = input("enter the character you want to replace  : ")

chooseword = input("enter the replaced word : ")

rep(str , final_string ,lee , replaceword , chooseword )




        