from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Servidor Flask rodando!'

@app.route('/dados', methods=['POST'])
def dados():
    data = request.json
    print("Recebido:", data)
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run()
