var CACHE_NAME = "django-pwa-v" + new Date().getTime();
var URL_TO_CACHE = [
    '/',
    'https://cdn.jsdelivr.net/npm/normalize.css@8.0.1/normalize.min.css',
    'https://cdn.jsdelivr.net/npm/glider-js@1.7.3/glider.min.css',
    '//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css',
    'https://code.jquery.com/jquery-1.12.4.js',
    'https://code.jquery.com/ui/1.12.1/jquery-ui.js',
    'https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/js/select2.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.9.2/html2pdf.bundle.js',
    '/static/css/jquery-ui.css',
    '/static/css/select2.css',
    '/static/css/style.css',
    '/static/css/tingle.css',
    '/static/img/favicon.ico',
    '/static/js/fn.js',
    '/static/js/glide.js',
    '/static/js/tingle.js',
    '/static/js/validacionRegistro.js',
    '/static/img/iconsPwa/1024.png',
    '/static/img/iconsPwa/512.png',
    '/static/img/iconsPwa/256.png',
    '/static/img/iconsPwa/128.png',
    '/static/img/iconsPwa/64.png',
    '/static/img/iconsPwa/32.png',
    '/static/img/iconsPwa/16.png'
];

// EVENTO 1 - SE ALMACENA EN CACHE LOS ARCHIVOS ESTATICOS PARA QUE FUNCIONE SIN INTERNET
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                return cache.addAll(URL_TO_CACHE);
            })
    )
});

// EVENTO 2 - ACTIVA Y BUSCA LOS RECURSOS PARA QUE FUNCIONE SIN INTERNET
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== CACHE_NAME))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// EVENTO 3 - CUANDO VUELVA A TENER INTERNET, ACTUALIZA LOS ARCHIVOS
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('offline');
            })
    )
});