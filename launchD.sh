#! /bin/sh

sudo touch /home/pi/Desktop/DiashowLaunch.txt
sudo python3 /home/pi/MessageSystem/startDiashow_DriveListener.py >> /home/pi/MessageSystem/log_diashow.txt
