#Main
import os
import time
check = False
while True:
    print("Checking if USB Drive media is available...")
    time.sleep(5)
    if(os.path.isdir("/media/pi/MEDIA1")==True):
        if(check==False):
            print("USB Drive media connected")
            os.system('sudo feh -F -x -R -w -Z -D 10 /media/pi/MEDIA1')
            check=True
        else:
            print("Please replug your USB Drive")
    else:
       if(os.path.isdir("/media/pi/MEDIA1")==False):
           check=False
           time.sleep(5)
           print("USB not connected")
           time.sleep(5)
           
