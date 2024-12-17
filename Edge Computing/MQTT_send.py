import paho.mqtt.client as mqtt
import base64
import time

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "weather/image"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def send_images(image_path, num_images):
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        encoded_image = base64.b64encode(image_data).decode('utf-8')

    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()

    for i in range(num_images):
        client.publish(MQTT_TOPIC, encoded_image)
        print(f"Sent image {i+1}")
        time.sleep(1)  # Small delay to ensure messages are sent properly

    client.loop_stop()

if __name__ == "__main__":
    image_path = "test.jpg"
    num_images = 1
    send_images(image_path, num_images)