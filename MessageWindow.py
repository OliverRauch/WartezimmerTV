#Programm um den naechsten Patienten aufzurufen
#by Oliver Rauch
#Imports
from tkinter import *
import sys
import time
import os

sleepTime = 15000

def create_Window():
    #File auslesen
    file = open("/home/pi/MessageSystem/text.txt", "r")
    x = file.read()

    #Frame erstellen
    App = Tk()
    labelfont = ('times', 20, 'bold')

    #Frame Size festlegen
    App.geometry("750x100+200+200")

    #Titel festlegen
    App.title("MessageWindow")

    #Text fuer Frame erstellen und einfuegen
    T = Text(App, height=100, width=100, font=("Helvetica", 30))
    T.pack()
    T.insert(END, x)
    T.insert(END, ", bitte kommen Sie herein!")

    #Fenster schliessen nach Delay
    App.after(sleepTime, lambda: App.destroy())
    App.mainloop()
#EndOfFunction

#Main
while True:
    if(os.path.isfile('/home/pi/MessageSystem/text.txt')==True):
        print("File text.txt detected")
        print("open Window...")
        create_Window()
        print("closed Window")
        time.sleep(3)
    else:
       time.sleep(3)