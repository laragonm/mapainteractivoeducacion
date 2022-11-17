// MAPA DE INICIO
let map = L.map('map').setView([12.9642272, -85.2047756], 8);

// CONFICURACION
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// ICONO DE CARGA
/*var icono = L.icon({
    iconUrl: 'https://e7.pngegg.com/pngimages/818/821/png-clipart-location-logo-duke-university-others-miscellaneous-blue.png',
    iconSize: [50, 50],
    iconAnchor: [22, 94]
});*/

// Colores por sub sistemas

var colorMined = "blue";
var colorCnu = "green";
var colorInatec = "yellow";

// UBICACIONES