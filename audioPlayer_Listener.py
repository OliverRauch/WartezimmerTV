#Main
import os
import time
check = False
while True:
    print("Checking if audio.mp3 is available...")
    time.sleep(5)
    if(os.path.isfile('/home/pi/MessageSystem/audio.mp3')==True):
            os.system('sudo mpg321 /home/pi/MessageSystem/audio.mp3')
            time.sleep(15)
       
           

