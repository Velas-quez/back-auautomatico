import json
from mqtt import send_mqtt, send_recieve_mqtt

### Agendamento recorrente
# Cada dispositivo só pode ter um, com até 5 horários no dia

def get_recurrent_schedule(device_code):
    response = send_recieve_mqtt(device_code, 'schedule/recurrent/get', "GET")
    return response

def set_recurrent_schedule(device_code, times, frequency):
    """Agenda um horário recorrente de alimentação, que tem início no dia que é configurado, 
    repete a cada "frequency" dias e alimenta nos horários "times" dos dias marcados."""
    
    payload = json.dumps({
        "times": times,
        "frequency": frequency
    })
    
    response = send_recieve_mqtt(device_code, 'schedule/recurrent/set', payload)
    return response
    
def delete_recurrent_schedule(device_code):
    response = send_recieve_mqtt(device_code, 'schedule/recurrent/delete', "DELETE")
    return response


### Agendamento específico
# Cada dispositivo pode ter até 5, com até 5 horários por agendamento

def get_independent_schedules(device_code):
    response = send_recieve_mqtt(device_code, 'schedule/independent/get', "GET")
    return response

def create_independent_schedule(device_code, day, times):
    payload = json.dumps({
        "day": day,
        "times": times
    })
    
    response = send_recieve_mqtt(device_code, 'schedule/independent/set', payload)
    return response

def delete_independent_schedule(device_code, schedule_id):
    payload = json.dumps({
        "schedule_id": schedule_id
    })
    
    response = send_recieve_mqtt(device_code, 'schedule/independent/delete', payload)
    return response
