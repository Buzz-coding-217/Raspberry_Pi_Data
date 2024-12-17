from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
import time


led = LED(15)

unit = 0.2

win = Tk()
win.title("Morse Code Generator")
win.geometry("455x223")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

def close():
    RPi.GPIO.cleanup()
    win.destroy()

def dot():
    led.on()   
    time.sleep(unit * 1)
    led.off()    
    time.sleep(unit * 1)
    
def slash():
    led.on()
    time.sleep(unit * 3)
    led.off()
    time.sleep(unit * 1)


def morse_code():
    text = text_box.get(1.0, "end-1c")
    for i in text:
      if i == 'a':
        dot()
        slash()
      elif i == 'b':
        slash()
        dot()
        dot()
        dot()
      elif i == 'c':
        slash()
        dot()
        slash()
        dot()
         
      elif i == 'd':
        slash()
        dot()
        dot()
         
      elif i == 'e':
        dot()
         
      elif i == 'f':
        slash()
        dot()
        dot()
        slash()
        dot()
         
      elif i == 'g':
        slash()
        slash()
        dot()
         
      elif i == 'h':
        dot()
        dot()
        dot()
        dot()
         
      elif i == 'i':
        dot()
        dot()
         
      elif i == 'j':
        dot()
        slash()
        slash()
        slash()
         
      elif i == 'k':
        slash()
        dot()
        slash()
         
      elif i == 'l':
        dot()
        slash()
        dot()
        dot()
         
      elif i == 'm':
        slash()
        slash()
         
      elif i == 'n':
        slash()
        dot()
         
      elif i == 'o':
        slash()
        slash()
        slash()
         
      elif i == 'p':
        dot()
        slash()
        slash()
        dot()
         
      elif i == 'q':
        slash()
        slash()
        dot()
        slash()
         
      elif i == 'r':
        dot()
        slash()
        dot()
         
      elif i == 's':
        dot()
        dot()
        dot()
         
      elif i == 't':
        slash()
         
      elif i == 'u':
        dot()
        dot()
        slash()
         
      elif i == 'v':
        dot()
        dot()
        dot()
        slash()
         
      elif i == 'w':
        dot()
        slash()
        slash()
         
      elif i == 'x':
        slash()
        dot()
        dot()
        slash()
         
      elif i == 'y':
        slash()
        dot()
        slash()
        slash()
         
      elif i == 'z':
        slash()
        slash()
        dot()
        dot()
         
    time.sleep(unit * 3)
def text_size(value):
    text_ = text_box.get('1.0','end-1c')
    breaks = text_.count('\n')
    t_size = len(text_) - breaks
    if t_size > 12:
        text_box.delete('end-2c')
    
Label(win, text="Enter the Text in the Textbox").pack()
text_box = Text(win, height = 5, width = 20)
text_box.pack()
text_box.bind('<KeyRelease>', text_size)
Button(win, text="Generate Morse Code",command = morse_code, font = myFont, bg = 'green').pack()
Button(win, text="Exit", font= myFont, command = close, bg='red').pack()

