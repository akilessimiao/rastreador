import time
import requests

API_URL = "http://127.0.0.1:5000/api/location"

# Rota simulada
route = [
    {"latitude": -23.55052, "longitude": -46.633308},
    {"latitude": -23.551111, "longitude": -46.634444},
    {"latitude": -23.552222, "longitude": -46.635555},
    {"latitude": -23.553333, "longitude": -46.636666},
]

for point in route:
    data = {
        "latitude": point["latitude"],
        "longitude": point["longitude"],
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        response = requests.post(API_URL, json=data)
        print(f"Enviando: {data} - Resposta: {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar dados: {e}")

    time.sleep(2)  # Aguardar 2 segundos
