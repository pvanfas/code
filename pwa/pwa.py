#project url
from django.views.generic import TemplateView

url(r'^manifest\.json$',TemplateView.as_view(template_name="manifest.json",content_type="text/javascript"),name='manifest'),
url(r'^sw\.js$',TemplateView.as_view(template_name="sw.js",content_type="text/javascript"),name='sw'),

#sw.js (add to templates)
var cacheName = 'Tutorial-v1';

var urlsToCache = [
    '/',

    '/static/css/app.css',
    '/static/css/app.min.1.css',
    '/static/css/app.min.2.css',
    '/static/css/demo.css',
];

self.addEventListener('install', function(event) {
    // Perform install steps
    console.log(cacheName + ' installing...');
    self.skipWaiting();

    event.waitUntil(
        caches.open(cacheName).then(function(cache) {
            console.log('Opened cache');
            cache.addAll(urlsToCache.map(function(urlsToCache) {
                return new Request(urlsToCache, { mode: 'no-cors' });
            })).then(function() {
                console.log('All resources have been fetched and cached.');
            });
        })
    );
});


self.addEventListener('activate', function(event) {

    var cacheWhitelist = ['Tutorial-v1',];

    event.waitUntil(
        caches.keys().then(function(cacheNames) {
            return Promise.all(
                cacheNames.map(function(cacheName) {
                    if (cacheWhitelist.indexOf(cacheName)  === -1) {
                        return caches.delete(cacheName);
                    }
                    console.log('activated');
                })
            );
        })
    );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(async function() {
    const cache = await caches.open('mysite-dynamic');
    const cachedResponse = await cache.match(event.request);
    const networkResponsePromise = fetch(event.request);

    event.waitUntil(async function() {
      const networkResponse = await networkResponsePromise;
      await cache.put(event.request, networkResponse.clone());
    }());

    // Returned the cached response if we have one, otherwise return the network response.
    return cachedResponse || networkResponsePromise;
  }());
});


function addToHomeScreen() {  var a2hsBtn = document.querySelector(".ad2hs-prompt");  // hide our user interface that shows our A2HS button
  a2hsBtn.style.display = 'none';  // Show the prompt
  deferredPrompt.prompt();  // Wait for the user to respond to the prompt
  deferredPrompt.userChoice
    .then(function(choiceResult){

  if (choiceResult.outcome === 'accepted') {
    console.log('User accepted the A2HS prompt');
  } else {
    console.log('User dismissed the A2HS prompt');
  }

  deferredPrompt = null;

});}

#manifest (add to templates)
{
  "name": "Tutorial",
  "short_name": "Tutorial",
  "theme_color": "#3a73a0",
  "background_color": "#3491db",
  "display": "standalone",
  "prompt-message" : "Add to home screen",
  "orientation" :"any",
  "Scope": "/",
  "start_url": "/",
  "icons": [
    {
      "src": "static/img/icons/icon-72x72.png",
      "sizes": "72x72",
      "type": "image/png"
    },
    {
      "src": "static/img/icons/icon-96x96.png",
      "sizes": "96x96",
      "type": "image/png"
    },
    {
      "src": "static/img/icons/icon-128x128.png",
      "sizes": "128x128",
      "type": "image/png"
    },
    {
      "src": "static/img/icons/icon-144x144.png",
      "sizes": "144x144",
      "type": "image/png"
    },
    {
      "src": "static/img/icons/icon-152x152.png",
      "sizes": "152x152",
      "type": "image/png"
    },
    {
      "src": "static/img/icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "static/img/icons/icon-384x384.png",
      "sizes": "384x384",
      "type": "image/png"
    },
    {
      "src": "static/img/icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "splash_pages": null
}

# icons (static/img/icons)

#base.html
<script type="text/javascript">

    if ('serviceWorker' in navigator) {
        window.addEventListener('load', function() {
            navigator.serviceWorker.register('/sw.js').then(function(registration) {
              // Registration was successful
              console.log('ServiceWorker registration successful with scope: ', registration.scope);
            }, function(err) {
              // registration failed :(
              console.log('ServiceWorker registration failed:', err);
            });
        });
    }

</script>

#link in base.html
<link rel="manifest" href="/manifest.json">