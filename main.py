from flask import Flask, request, jsonify
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
import logging

from feed import feed_instant
from level_inspect import get_pot_level, get_reservatory_level
from schedule_feed import create_independent_schedule, delete_independent_schedule, delete_recurrent_schedule, get_independent_schedules, get_recurrent_schedule, set_recurrent_schedule

app = Flask(__name__)
CORS(app,supports_credentials=True)
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
    device_code = request.args.get('device_code')
    if not device_code:
        return jsonify({"error": "Parâmetro de rota 'device_code' faltando"}), 400
    result = get_pot_level(device_code)
    return jsonify(result), 200

@app.route('/inspect-level/reservatory', methods=['GET'])
def inspect_reservatory_level_route():
    device_code = request.args.get('device_code')
    if not device_code:
        return jsonify({"error": "Parâmetro de rota 'device_code' faltando"}), 400
    result = get_reservatory_level(device_code)
    return jsonify(result), 200


# SCHEDULE SINGLE
@app.route('/independent-schedules', methods=['GET'])
def get_independent_schedule_route():
    device_code = request.args.get('device_code')
    if not device_code:
        return jsonify({"error": "Parâmetro de rota 'device_code' faltando"}), 400
    result = get_independent_schedules(device_code)
    return jsonify(result), 200

@app.route('/independent-schedules/create', methods=['POST'])
def create_independent_schedule_route():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "JSON inválido ou ausente"}), 400
    day = data.get('day')
    times = data.get('times')
    device_code = data.get('device_code')
    if not device_code or day is None or times is None:
        return jsonify({"error": "Parâmetros faltando"}), 400
    result = create_independent_schedule(device_code, day, times)
    return jsonify(result), 200

@app.route('/independent-schedules/delete', methods=['DELETE'])
def delete_independent_schedule_route():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "JSON inválido ou ausente"}), 400
    device_code = data.get('device_code')
    schedule_id = data.get('schedule_id')
    if not device_code or schedule_id is None:
        return jsonify({"error": "Parâmetros faltando"}), 400
    result = delete_independent_schedule(device_code, schedule_id)
    return jsonify(result), 200


# SCHEDULE RECURRENT
@app.route('/recurrent_schedule', methods=['GET'])
def get_recurrent_schedule_route():
    device_code = request.args.get('device_code')
    if not device_code:
        return jsonify({"error": "Parâmetro de rota 'device_code' faltando"}), 400
    result = get_recurrent_schedule(device_code)
    return jsonify(result), 200

@app.route('/recurrent_schedule/set', methods=['POST'])
def set_recurrent_schedule_route():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "JSON inválido ou ausente"}), 400
    frequency = data.get('frequency')
    times = data.get('times')
    device_code = data.get('device_code')
    if not device_code or frequency is None or times is None:
        return jsonify({"error": "Parâmetros faltando"}), 400
    result = set_recurrent_schedule(device_code, times, frequency)
    return jsonify(result), 200

@app.route('/recurrent_schedule/delete', methods=['DELETE'])
def delete_recurrent_schedule_route():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "JSON inválido ou ausente"}), 400
    device_code = data.get('device_code')
    if device_code is None:
        return jsonify({"error": "Parâmetros faltando"}), 400
    result = delete_recurrent_schedule(device_code)
    return jsonify(result), 200

# HOME
@app.route('/')
def home():
    return "AuAu!"



if __name__ == "__main__":
    app.run(host='0.0.0.0')