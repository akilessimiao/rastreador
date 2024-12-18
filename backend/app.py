from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir requisições do front-end

# Criar o banco de dados se ele não existir
def init_db():
    conn = sqlite3.connect('tracking.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            timestamp DATETIME NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Endpoint para receber dados do rastreador (POST)
@app.route('/api/location', methods=['POST'])
def receive_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    timestamp = data.get('timestamp')

    conn = sqlite3.connect('tracking.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO locations (latitude, longitude, timestamp) VALUES (?, ?, ?)",
        (latitude, longitude, timestamp)
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Location saved successfully'}), 200

# Endpoint para buscar a última localização (GET)
@app.route('/api/latest-location', methods=['GET'])
def get_latest_location():
    conn = sqlite3.connect('tracking.db')
    cursor = conn.cursor()
    cursor.execute("SELECT latitude, longitude, timestamp FROM locations ORDER BY id DESC LIMIT 1")
    location = cursor.fetchone()
    conn.close()
    if location:
        return jsonify({
            "latitude": location[0],
            "longitude": location[1],
            "timestamp": location[2]
        })
    return jsonify({"message": "No data found"}), 404

if __name__ == '__main__':
    init_db()  # Inicializar o banco de dados
    app.run(host='0.0.0.0', port=5000, debug=True)
