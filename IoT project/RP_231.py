import paho.mqtt.client as mqtt
import random
import time

# MQTT broker information
mqtt_broker_host = "mqtt://broker.hivemq.com"
mqtt_broker_port = 1883  # Default MQTT port
mqtt_topic = "mqtt/RP/4322"

# Create an MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect("broker.hivemq.com", mqtt_broker_port, 60)

# Function to publish random data
def publish_data():
    random_value = random.randint(0, 1)  # Generates either 0 or 1
    message = "ON" if random_value == 0 else "OFF"
    client.publish(mqtt_topic, message)
    print(f"Data published to MQTT topic: {message}")

try:
    # Loop to publish data indefinitely
    while True:
        publish_data()
        time.sleep(3)  # Sleep for 3 seconds

except KeyboardInterrupt:
    print("Publishing stopped by the user.")
    client.disconnect()
