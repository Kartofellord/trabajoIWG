mapboxgl.accessToken = 'pk.eyJ1Ijoib3ByYWRvIiwiYSI6ImNsbnh5ajc0MjBqZmUybGxqYWFoMG9tMGUifQ.00CFhrjNRQpCyBQDBuCpSg';
    const map = new mapboxgl.Map({
    container: 'map', // container ID
    style: 'mapbox://styles/oprado/clo07xyim00ao01qpfls54kj7/draft', // style URL
    center: [-35, 25], // starting position [lng, lat]
    zoom: 2.3 // starting zoom
    });

    // At low zooms, complete a revolution every two minutes.
    const secondsPerRevolution = 40;
    // Above zoom level 5, do not rotate.
    const maxSpinZoom = 3;
    // Rotate at intermediate speeds between zoom levels 3 and 5.
    const slowSpinZoom = 2.5;

    let userInteracting = false;

    function spinGlobe() {
        const zoom = map.getZoom();
        if (!userInteracting && zoom < maxSpinZoom) {
            let distancePerSecond = 180 / secondsPerRevolution;
            if (zoom > slowSpinZoom) {
                // Slow spinning at higher zooms
                const zoomDif = (maxSpinZoom - zoom) / (maxSpinZoom - slowSpinZoom);
                distancePerSecond *= zoomDif;
                }
            const center = map.getCenter();
            center.lng -= distancePerSecond;
            // Smoothly animate the map over one second.
            // When this animation is complete, it calls a 'moveend' event.
            map.easeTo({ center, duration: 1000, easing: (n) => n });
            }
        }

    // Pause spinning on interaction
    map.on('mousedown', () => {
    userInteracting = true;
    });

    map.on('mouseup', () => {
    userInteracting = false;
    setInterval(spinGlobe,7000)
    });

    map.on('dragend', () => {
    userInteracting = false;
    setInterval(spinGlobe,7000)
    });

    map.on('pitchend', () => {
    userInteracting = false;
    setInterval(spinGlobe,7000)
    });

    map.on('rotateend', () => {
    userInteracting = false;
    setInterval(spinGlobe,7000)
    });

    map.on('moveend', () => {
    spinGlobe()
    });

    spinGlobe();
 
    fetch('markers')
    .then(response => response.json())
    .then(data => {
        // data is the GeoJSON object from the server

        // add markers to map
        for (const feature of data.features) {
            // create a HTML element for each feature
            const el = document.createElement('div');
            el.className = 'marker';

            // make a marker for each feature and add to the map
            new mapboxgl.Marker(el).setLngLat(feature.geometry.coordinates)
            new mapboxgl.Marker(el)
            .setLngLat(feature.geometry.coordinates)
            .setPopup(
            new mapboxgl.Popup({ offset: 25 }) // add popups
            .setHTML(
                `<h3>${feature.properties.title}</h3><p>${feature.properties.description}</p>`
            )
            )
            .addTo(map);
        }
    });