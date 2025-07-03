from mqtt import send_recieve_mqtt


def get_pot_level(device_code):
    if device_code == "ABCD-01":
        return {"level": "mocked", "value": 42}
    response = send_recieve_mqtt(device_code, 'inspect/pot', "GET")
    return response

def get_reservatory_level(device_code):
    if device_code == "ABCD-01":
        return {"level": "mocked", "value": 99}
    response = send_recieve_mqtt(device_code, 'inspect/reservatory', "GET")
    return response