import RPi.GPIO as GPIO
import time

# Set the GPIO mode and the pin number for the button
GPIO.setmode(GPIO.BCM)
button_pin = 18

# Function to be called when the button is pressed
def on_button_press(channel):
    print("Button pressed!")

# Configure the GPIO pin for input and add event detection
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button_pin, GPIO.RISING, callback=on_button_press, bouncetime=200)

# Main loop to keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
