# here we wil append string in python 

str1 = "Vansh "
len1 = len(str1)
str2 = "joshi"
len2 = len(str2)
str3 = []

def append(s1, l1 , s2 , l2 , s3):
    
    for i in range(0,l1):
        s3.append(s1[i])

    for j in range(0,l2):
        s3.append(s2[j])

append(str1 , len1 , str2 , len2 , str3)


print(str3)
print(''.join(str3))   # this is how we convert list into string 