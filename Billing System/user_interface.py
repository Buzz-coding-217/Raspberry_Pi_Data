from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

green = LED(17)
blue = LED(18)
red = LED(15)


win = Tk()
win.title("LEDs Toggler")
win.geometry("455x180")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

def red_on():
    blue.off()
    red.on()
    green.off()
    

def green_on():
    blue.off()
    red.off()
    green.on()
    
def blue_on():
    blue.on()
    red.off()
    green.off()
    
def off_all():
    blue.off()
    red.off()
    green.off()

def close():
    RPi.GPIO.cleanup()
    win.destroy()

var = tkinter.IntVar()

    
Label(win, foreground = 'black',text="Which color LED you want to switch on?").pack()
radio = Radiobutton(win, padx=14,text="Red",bg = 'red' ,variable = var,value = 1,command = red_on).pack(anchor="w")
radio = Radiobutton(win, padx=14,text="Green",bg = 'green' ,variable = var,value = 2, command = green_on).pack(anchor="w")
radio = Radiobutton(win, padx=14, text="Blue",bg = 'blue' ,variable = var,value = 3,command = blue_on).pack(anchor="w")
radio = Radiobutton(win, padx=14, text="None",bg = 'white' ,variable = var,value = 4,command = off_all).pack(anchor="w")
Button(win, foreground = 'white',text="Exit", font= myFont, command = close, bg='red').pack()

