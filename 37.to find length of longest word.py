# a program to find length of longest word in python 



str = "this is a string" 

str2 = "  ;:,." 
words = [] 
word_count = ""


for ch in str:
    if ch in str2 :
        if word_count:
            words.append(word_count) 
            word_count = "" 


    else:
        word_count = word_count + ch


if word_count:
    words.append(word_count)



if words:
    max_length = max(len(word) for word in words)
    print(max_length)



