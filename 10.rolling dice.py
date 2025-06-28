# throw a dice 

import math
import random

while(True):
    ask  = int(input("enter 1 to play \n0 to exit\n"))

    if(ask == 1):
        print("DICE:", random.randint(1,6))
    

    else:
        print("thx for playing , you exited")
        break
    






