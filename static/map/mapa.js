// MAPA DE INICIO
let map = L.map('map').setView([13.085764, -86.355183],14);

// CONFICURACION
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

document.getElementById('select-location').addEventListener('change', function (e) {
    let coords = e.target.value.split(",");
    map.flyTo(coords, 13);
});

// ICONO DE CARGA
var icono = L.icon({
    iconUrl: 'https://e7.pngegg.com/pngimages/818/821/png-clipart-location-logo-duke-university-others-miscellaneous-blue.png',
    iconSize: [50, 50],
    iconAnchor: [22, 94]
});

// Colores por sub sistemas

var colorMined = "blue";
var colorCnu = "green";
var colorInatec = "yellow";

// UBICACIONES

// UBICACION DE BOACO

var Boaco = L.marker(L.latLng(12.477575, -85.673815), {
    radius: 10,
    fillColor: colorMined,
    color: "black",
    weight: 2,
    opacity: 1,
    fillOpacity: 0.0,
    icon: icono
}).addTo(map);

// UBICACION DE MANAGUA
var Managua = L.marker(L.latLng(12.100080, -86.252990), {
    radius: 10,
    fillColor: colorCnu,
    color: "black",
    weight: 2,
    icon:icono
}).addTo(map);

// UBICACION DE RIVAS
var rivas = L.marker(L.latLng(12.9276412, -85.9179257), {
    radius: 10,
    fillColor: colorInatec,
    color: "black",
    weight: 2,
    icon:icono
}).addTo(map);

// MENSAJE POPUP BOACO
Boaco.bindPopup("<h1><h1>Boaco</h1><h2>Ciudad de dos pisos</h2><h3>Pagina oficial: " +
    "<a href='www.google.com'>Boaco.com</a></h3>").openPopup();

// MENSAJE POPUP MANAGUA
Managua.bindPopup("<h1>Managua</h1><h2>Tierra de volcanes</h2><h3>Pagina oficial: " +
    "<a href='www.google.com'> Managua.com</a></h3>").openPopup();