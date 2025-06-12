from mqtt import send_recieve_mqtt


def get_pot_level(device_code):
    response = send_recieve_mqtt(device_code, 'inspect/pot', "GET")
    return response

def get_reservatory_level(device_code):
    response = send_recieve_mqtt(device_code, 'inspect/reservatory', "GET")
    return response