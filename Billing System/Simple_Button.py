from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

ledButton = Button(win, text = "Press here", font = myFont, bg = 'bisque', height = 1, width = 24)
ledButton.grid(row=0,column=1)
