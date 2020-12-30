"use strict";
google.maps.event.addDomListener(window, "load", function () {
  var myLatLng = {
    lat: -0.3442956,
    lng: -78.5673983
  };
  var mapOptions = {
    zoom: 15,
    center: myLatLng
  };
  var mapa_element = document.getElementById('map');
  var map = new google.maps.Map(mapa_element, mapOptions);

  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    draggable: true,
    animation: google.maps.Animation.Drop,
    title: "mi casa"
  });

  marker.addListener('dragend', function (event) {
    console.log(marker.getPosition().lat() + "," + marker.getPosition().lng());
  });
});
