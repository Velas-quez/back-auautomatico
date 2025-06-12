from mqtt import send_mqtt


def feed_instant(portion, device_code):
    response = send_mqtt(device_code=device_code, topic="feed/instant", message=portion)
    return response.is_published()