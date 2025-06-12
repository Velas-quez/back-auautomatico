import time
import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv
import threading

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

def send_recieve_mqtt(device_code, topic, message, qos=1, timeout=120):
    client = mqtt.Client()
    client.username_pw_set(USER, PASS)
    client.tls_set()
    
    response_topic = f"{device_code}/response/{topic}"
    message_id = str(int(time.time() * 1000))
    event = threading.Event()
    response = {'payload': None}
    
    def on_connect(c, userdata, flags, rc, properties=None):
        client.subscribe(response_topic, qos=qos)
    
    def on_message(c, userdata, msg):
        # você pode validar message_id se incluir no payload
        response['payload'] = msg.payload.decode()
        event.set()
        c.loop_stop()
    
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(BROKER, PORT)
    client.loop_start()
    
    full_topic = f"{device_code}/command/{topic}"
    client.publish(full_topic, message, qos=qos)
    
    received = event.wait(timeout=timeout)
    
    client.disconnect()
    if not received:
        raise TimeoutError(f"Sem resposta em {timeout}s no tópico {response_topic}")
    
    return response['payload']