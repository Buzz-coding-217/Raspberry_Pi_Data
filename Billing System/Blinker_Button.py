from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

green = LED(17)
blue = LED(18)
red = LED(15)


win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

def greenToggle():
    if green.is_lit:
        green.off()
    else:
        green.on()

def blueToggle():
    if blue.is_lit:
        blue.off()
    else:
        blue.on()
        
def redToggle():
    if red.is_lit:
        red.off()
    else:
        red.on()

ledButton = Button(win, text = "Red",command = redToggle, font = myFont, bg = 'bisque', height = 1, width = 24)
ledButton.grid(row=0,column=1)

ledButton = Button(win, text = "Blue",command = blueToggle, font = myFont, bg = 'bisque', height = 1, width = 24)
ledButton.grid(row=1,column=1)

ledButton = Button(win, text = "green",command = greenToggle,  font = myFont, bg = 'bisque', height = 1, width = 24)
ledButton.grid(row=2,column=1)