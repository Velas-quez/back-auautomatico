from mqtt import send_mqtt

### Agendamento recorrente
# Cada dispositivo só pode ter um, com até 5 horários no dia

def get_recurrent_schedule(device_code):
    return "Not implemented"

def set_recurrent_schedule(device_code, times, frequency):
    """Agenda um horário recorrente de alimentação, que tem início no dia que é configurado, 
    repete a cada "frequency" dias e alimenta nos horários "times" dos dias marcados."""
    
def delete_recurrent_schedule(device_code):
    return "Not implemented"


### Agendamento específico
# Cada dispositivo pode ter até 5, com até 5 horários por agendamento

def get_independent_schedules(device_code):
    return "Not implemented"

def create_independent_schedule(device_code, day, times):
    return "Not implemented"

def delete_independent_schedule(device_code, schedule_id):
    return "Not implemented"
