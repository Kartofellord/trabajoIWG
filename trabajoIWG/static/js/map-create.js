mapboxgl.accessToken = 'pk.eyJ1Ijoib3ByYWRvIiwiYSI6ImNsbnh5ajc0MjBqZmUybGxqYWFoMG9tMGUifQ.00CFhrjNRQpCyBQDBuCpSg';
    const map = new mapboxgl.Map({
    container: 'map', // container ID
    style: 'mapbox://styles/oprado/clo07xyim00ao01qpfls54kj7/draft', // style URL
    center: [-35, 25], // starting position [lng, lat]
    zoom: 2.3 // starting zoom
    });
