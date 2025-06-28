# to check  whetehr a given year is leap year or not 

def leapyear( year):
    if(year%4 !=0):
        return False
    
    elif(year%100 !=0):
        return True
    
    elif(year%400 !=0):
        return False
    
    else:
        return True
    


for i in range(2000 , 2100):
    if(leapyear(i)== True):
        print(f'{i} LEAPYEAR')

    else:
        print(f'{i}')
    

