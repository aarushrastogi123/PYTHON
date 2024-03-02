import time as t
time=t.strftime('%H:%M:%S')
print('Time=',time)
hour=int(t.strftime('%H'))
print('Hour=',hour)
minutes=int(t.strftime('%M'))
print('Minutes=',minutes)
seconds=int(t.strftime('%S'))
print('Seconds=',seconds)

import datetime
def find_day():
    day=datetime.datetime.today().weekday()
     
    if day==0:
        return 'MONDAY'
    elif day==1:
        return 'TUESDAY'
    elif day==2:
        return 'WEDNESDAY'
    elif day==3:
        return 'THURSDAY'
    elif day==4:
        return 'FRIDAY'
    elif day==5:
        return 'SATURDAY'
    elif day==6:
        return 'SUNDAY' 
print(find_day())    


if(hour<12):
    print("GOOD MORNING AARUSH")
elif(12<=hour<16):
    print("GOOD AFTERNOON AARUSH")
elif(16<=hour<21):
    print("GOOD EVENING AARUSH")
elif(21<=hour<24):
    print("GOOD NIGHT AARUSH")
else:
    print("")        
            
          
          

    
          