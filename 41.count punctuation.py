# a program to count the punctuations 

str = "this, is a ahhhh......"
s2 = ",.:;"


l = len(str) 
l2 = len(s2)


def punctuation(s , l , s2 , l2):
    count = 0

    for i in range(0, l):
        m = s[i] 
        for j in range(0 , l2):
            if(m == s2[j]):
                count = count + 1


    return count 



print(punctuation(str , l , s2 , l2))
