from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import time
import paho.mqtt.client as mqtt

app = Flask(__name__)
sched = BackgroundScheduler(daemon=True)
sched.start()

# MQTT HiveMQ Cloud
BROKER = "40ee48e1dc244790b777f0d2e77cc32e.s1.eu.hivemq.cloud"
PORT = 8883
USER = "hivemq.webclient.1749645042519"
PASS = "?EW!oU*kj1ry7@0xSR8C"
TOPIC = "casa/comando/led"

def trigger_led():
    client = mqtt.Client()
    client.username_pw_set(USER, PASS)
    client.tls_set()
    client.connect(BROKER, PORT)
    client.publish(TOPIC, "ON", qos=1)
    client.disconnect()

@app.route('/led-delay', methods=['POST'])
def led_delay():
    run_time = time.time() + 5 * 60
    sched.add_job(trigger_led, 'date', run_date=time.strftime(
        '%Y-%m-%d %H:%M:%S', time.localtime(run_time)))
    return jsonify({"scheduled_in": "5 minutes"})

@app.route('/')
def home():
    return "Backend Flask MQTT ativo!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')