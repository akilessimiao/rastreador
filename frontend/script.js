// Configuração inicial do mapa
var map = L.map('map').setView([-23.55052, -46.633308], 13); // Posição inicial (São Paulo)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

// Adicionar marcador
var marker = L.marker([-23.55052, -46.633308]).addTo(map);

// Função para buscar a última localização da API
function fetchLatestLocation() {
    fetch('http://127.0.0.1:5000/api/latest-location')
        .then(response => response.json())
        .then(data => {
            if (data.latitude && data.longitude) {
                var lat = data.latitude;
                var lng = data.longitude;
                var timestamp = data.timestamp;

                // Atualizar posição do marcador
                marker.setLatLng([lat, lng]);
                map.setView([lat, lng], 15);
                console.log(`Última localização: Latitude ${lat}, Longitude ${lng}, Hora: ${timestamp}`);
            }
        })
        .catch(error => console.error("Erro ao buscar dados:", error));
}

// Atualizar o mapa a cada 3 segundos
setInterval(fetchLatestLocation, 3000);
