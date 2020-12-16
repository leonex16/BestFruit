const CACHE_NAME = 'v1_cache_bestFruit';
const URL_TO_CACHE = [
    '/',
    'https://cdn.jsdelivr.net/npm/normalize.css@8.0.1/normalize.min.css',
    'https://cdn.jsdelivr.net/npm/glider-js@1.7.3/glider.min.css',
    '//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css',
    'https://code.jquery.com/jquery-1.12.4.js',
    'https://code.jquery.com/ui/1.12.1/jquery-ui.js',
    'https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/js/select2.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.9.2/html2pdf.bundle.js',
    '../css/jquery-ui.css',
    '../css/select2.css',
    '../css/style.css',
    '../css/tingle.css',
    '../img/favicon.ico',
    '../js/fn.js',
    '../js/glide.js',
    '../js/tingle.js',
    '../js/validacionRegistro.js'
];

// EVENTO 1 - SE ALMACENA EN CACHE LOS ARCHIVOS ESTATICOS PARA QUE FUNCIONE SIN INTERNET
self.addEventListener('install', e => {
    e.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                return cache.addAll(URL_TO_CACHE)
                    .then(() => self.skipWaiting())
            })
            .catch(err => console.warn('Error con el cache : ', err))
    )
});

// EVENTO 2 - ACTIVA Y BUSCA LOS RECURSOS PARA QUE FUNCIONE SIN INTERNET
self.addEventListener('activate', e=> {
    const CACHE_WHITE_LIST = [CACHE_NAME];
    e.waitUntil(
        caches.keys()
            .then(cachesNames => {
                cachesNames.map(cachesName =>{
                    if(CACHE_WHITE_LIST.indexOf(cachesName) === -1){
                        return caches.delete(cachesName)
                    }
                })
            })
            .then(() => self.clients.claim())
    )
});

// EVENTO 3 - CUANDO VUELVA A TENER INTERNET, ACTUALIZA LOS ARCHIVOS
self.addEventListener('fetch', e=> {
    e.respodWith(
        caches.match(e.request)
            .then(res => {
                if(res) return res

                return fetch(e.request)
            })
    )
});
