# program to check that given number is uppercase or lowercase 


def uprorlwr(n):
    if(n.isupper()):
        print('given text is in uppercase')

    else:
        print("given text is in lowercase")
        


str = input("enter the text: \n")


uprorlwr(str)