import time
import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

load_dotenv()

BROKER = os.getenv("MQTT_BROKER")
PORT = int(os.getenv("MQTT_PORT", 8883))
USER = os.getenv("MQTT_USER")
PASS = os.getenv("MQTT_PASS")

def send_mqtt(device_code, topic, message, qos = 1):
    client = mqtt.Client()
    client.username_pw_set(USER, PASS)
    client.tls_set()
    client.connect(BROKER, PORT)
    client.loop_start()

    result = client.publish(device_code+"/"+topic, message, qos)

    result.wait_for_publish()
    time.sleep(0.1)

    client.loop_stop()
    client.disconnect()
    
    return result
