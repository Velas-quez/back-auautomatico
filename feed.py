import json
from mqtt import send_mqtt


def feed_instant(device_code, portion):
    if device_code == "ABCD-01":
        return True  # ou qualquer valor mockado desejado
    payload = json.dumps({
        "portion": portion
    })
    response = send_mqtt(device_code=device_code, topic="feed/instant", message=payload)
    return response.is_published()