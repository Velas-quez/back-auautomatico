import json
from mqtt import send_mqtt


def feed_instant(device_code, portion):
    payload = json.dumps({
        "portion": portion
    })
    response = send_mqtt(device_code=device_code, topic="feed/instant", message=payload)
    return response.is_published()