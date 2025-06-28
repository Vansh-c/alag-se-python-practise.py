# to check whether entered number is palindrome or not 
import math

def ispalindrome(num):
    rev = 0 

    while(num!=0):
        rem = num%10 
        rev = rev*10 + rem
        num = math.floor(num/10)


    return rev


n = int(input("enter  a number: "))

r = ispalindrome(n)
print(r)

if(r == n):
    print("enter number is a palindrome")

else:
    print("enter number is not a palindrome")