# Importing Libraries
import smbus # For creating bus instances 
import time

DEVICE = 0x23 # I2C device address
# Measurement with high resolution (1lx) and switching the device off after using
ONE_TIME_HIGH_RES_MODE = 0x20 
 
# Accessing the device in I2C address detect
bus = smbus.SMBus(1)  
 

# Function to read data from device
def readLight(addr=DEVICE):
  # Reading the measurement from device with address and resolution speed
  reading = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
  # Converting the reading to decimal number from 2 byte data
  result = ((reading[1] + (256 * reading[0])) / 1.2)
  return result
 
  
# Entry point
if __name__=="__main__":
   while True:
       # Reading the value and displaying on the serial monitor
       value = readLight()
       print ("Light Intensity: " + str(value) + " lux")
       # Printing the result category
       if(value < 3):
           print("Too Dark")
       elif(value < 10 and value > 3):
           print("Dark")
       elif(value < 20 and value > 10):
           print("Medium")
       elif(value < 25 and value > 20):
           print("Light")
       else:
           print("Too Light")
        # delay of 1 second
       time.sleep(1.0)
       
        