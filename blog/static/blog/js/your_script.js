// Initialize the map
function initMap() {
    // Specify the coordinates for the center of the map
    var myLatLng = {lat: -33.867, lng: 151.195};

    // Create a new map instance
    var map = new google.maps.Map(document.getElementById('map-container'), {
        zoom: 15,  // Adjust zoom level as needed
        center: myLatLng
    });

    // Create a new marker and set its position
    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'Hello World!'
    });
}
