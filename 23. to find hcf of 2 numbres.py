# here we will write a program to find hcf of two numbers 

def hcf(x ,y):
  while(x!=y):
      if(x>y):
        hcf(x-y , y)

      else:
        hcf(x , y-x)

  return x


a = int(input("enter value of x : "))
b = int(input("enter value of y:  "))


print(hcf(a , b))