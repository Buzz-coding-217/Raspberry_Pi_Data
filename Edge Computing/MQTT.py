import paho.mqtt.client as mqtt
import base64
import os

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "image/topic"
SAVE_DIR = "received_images"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print("Image received")
    payload = msg.payload.decode('utf-8')
    image_name, encoded_image = payload.split(":", 1)
    image_data = base64.b64decode(encoded_image)
    save_path = os.path.join(SAVE_DIR, image_name)
    with open(save_path, "wb") as image_file:
        image_file.write(image_data)
    print(f"Saved {image_name}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
