# to find length of smallest word in a string 


s = "this is a string" 
s2 = " ,:;."


current_word = ""
words = []



for ch in s:
    if ch in s2:
        if current_word:             # prevents adding character if there is an empty current word 
            words.append(current_word)   
            current_word = ""

    else:
        current_word+= ch


if words:
    min_len = min(len(word) for word in words ) 
    print(min_len)