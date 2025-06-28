# this program is used to convert from upper to lower and vice versa 


def conversion(n):
    if(n.isupper()):
        print("now given text is changed into lowercase")
        print(n.lower())

    else:
        print("now the given text is changed into uppercase")
        print(n.upper())



enter = input("please enter something ")
conversion(enter)





