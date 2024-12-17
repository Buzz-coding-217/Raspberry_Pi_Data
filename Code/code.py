import time
import pymongo

# Connect the motion sensor to GPIO pin 4
motion_sensor = MotionSensor(4)

mongo_uri = 'mongodb+srv://sahil:sahil@cluster0.9jyd2nq.mongodb.net/'

client = pymongo.MongoClient(mongo_uri)
db = client['Motion_Sensor_Data']
collection = db['motion_data']

try:
    while True:
        if motion_sensor.motion_detected:
            print("Motion Detected!")
            motion_status = "Motion Detected"
        else:
            print("No Motion.")
            motion_status = "Motion Not Detected"
            
        data = {
            'motion_status': motion_status
        }

        # Insert the data into the MongoDB collection
        collection.insert_one(data)

        time.sleep(2)  

except KeyboardInterrupt:
    print("Exiting....")