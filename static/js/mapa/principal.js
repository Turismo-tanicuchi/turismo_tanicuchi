"use strict";
google.maps.event.addDomListener(window, "load", function () {
  //diccionario de direcciones
  var atractivos_turisticos = [
    {nombre: 'a',lat: -0.7568866, lng: -78.6876387},
    {nombre: 'b',lat: -0.7814909, lng: -78.6390747},
    {nombre: 'c',lat: -0.9232388, lng: -78.6646051},
    {nombre: 'd',lat: -0.8400983, lng: -78.6674629},
    {nombre: 'f',lat: -0.8594118, lng: -78.9128209}
  ];

//posicion para centrar el mapa
  var toacazo ={
    lat: -0.7571307,
    lng: -78.6876387
  };
//opciones que tendra el mapa zoom y corrdenadas para centrarse
  var mapOptions = {
    zoom: 11,
    center: toacazo
  };
//capturar elemento html donde se mostrara el mapa
  var mapa_element = document.getElementById('map');
//mostrar el mapa
  var map = new google.maps.Map(mapa_element, mapOptions);
//marcadores
  for(var i in atractivos_turisticos){
    var marker = new google.maps.Marker({
        position: atractivos_turisticos[i],
        map: map,
        title: atractivos_turisticos[i].nombre,
    });
  }
});
