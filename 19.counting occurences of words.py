# to count the occurence of a word in a sentence 

def occurence(sent , word):
    l1 = len(sent) 
    l2 = len(word) 
    l3 = l1 - l2 +1 
    count = 0

    for i in range(0 , l3):
        t = True 

        for j in range(0 , l2):
            if(word[j] != sent[j+i]):
                t = False 
                j = j+1

        if(t):
            count+=1

    return count



 

s = input("enter a string : ")
word = input('enter a word : ')


print("occurence: " , occurence(s, word))