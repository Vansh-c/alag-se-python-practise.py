# making a dice roll function  using oops 

import  random 

class dice_roll:

        
    def playgame(self):
        while(True):
            ask = int(input("enter 1 to play\n0 to exit\n"))
            
            if(ask==1):
                print("DICE : " , random.randint(1,6))
                
            else:
                print("it was good game , thx for playing") 
                break 
            
dice = dice_roll()
dice.playgame()
            
            
            
            
        