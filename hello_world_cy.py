'''
My first code. 

@author JGraham
created 25/06/19
'''
import datetime
current_time = datetime.datetime.now()


if current_time.hour < 12:
    print("Bore da")
elif current_time.hour < 18:
    print("Prynhawn da")
else:
    print("Noswaith da")
