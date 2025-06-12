from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import logging

from feed import feed_instant

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
sched = BackgroundScheduler(daemon=True)
sched.start()


@app.before_request
def log_request_info():
    app.logger.debug("Request headers: %s", request.headers)
    app.logger.debug("Request body: %s", request.get_data())


# FEED INSTANT
@app.route('/feed-instant', methods=['POST'])
def feed_instant_route():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "JSON inválido ou ausente"}), 400

    device_code = data.get('device_code')
    portion = data.get('portion')
    if not device_code or portion is None:
        return jsonify({"error": "Parâmetros faltando"}), 400

    result = feed_instant(device_code, portion)

    return jsonify({"result": result}), 200


# INSPECT LEVELS
@app.route('/inspect-level/pot', methods=['GET'])
def inspect_pot_level_route():
    return "Not implemented"


# SCHEDULE SINGLE
@app.route('/independent-schedules', methods=['GET'])
def get_independent_schedule_route():
    return "Not implemented"

@app.route('/independent-schedules/create', methods=['POST'])
def create_independent_schedule_route():
    return "Not implemented"

@app.route('/independent-schedules/delete', methods=['DELETE'])
def delete_independent_schedule_route():
    return "Not implemented"


# SCHEDULE RECURRENT
@app.route('/recurrent_schedule', methods=['GET'])
def get_recurrent_schedule_route():
    return "Not implemented"

@app.route('/recurrent_schedule/set', methods=['POST'])
def set_recurrent_schedule_route():
    return "Not implemented"

@app.route('/recurrent_schedule/delete', methods=['DELETE'])
def delete_recurrent_schedule_route():
    return "Not implemented"

# HOME
@app.route('/')
def home():
    return "AuAu!"



if __name__ == "__main__":
    app.run(host='0.0.0.0')