function redireccionar(rol){
    switch (rol) {
        case '1': // Administrador
            return '/superAdmin/estadisticas/';
    
        case '2': // Cliente_externo
            return '/usuario/solicitud/';

        case '3': // Comerciante
            return '/usuario/historial/';

        case '4': // Productor
            return '/usuario/publicacion/';
    }
};

function btnRol(rol, btnAside){
    const $contenedorBaseHtml = document.querySelector('.usuario-contenedor');
    const $btn = btnAside;
    const $contenedorHistorialComerciante = document.querySelector('.historialComerciante-contenedor');
    const $contenedorHistorialExterno = document.querySelector('.historialExterno-contenedor');
    const $contenedorHistorialProductor = document.querySelector('.historialProductor-contenedor');

    const paths = {
        'solicitud': 'usuario/solicitud/',
        'pedido': 'usuario/pedido/',
        'historial': 'usuario/historial/',
        'informacion': 'usuario/informacion/',
        'publicacion': 'usuario/publicacion/'
    };

    switch (rol) {
        case 2:
            if (location.pathname.indexOf(paths['pedido']) === -1 &&
                location.pathname.indexOf(paths['historial']) === -1 &&
                location.pathname.indexOf(paths['informacion']) === -1 &&
                location.pathname.indexOf(paths['solicitud']) === -1) {
                $contenedorBaseHtml.remove();
            }
            $btn.removeChild($btn.children[2]);
            $btn.children[2].querySelector('span').textContent += ' Pedidos';
            $btn.classList.add('grid-cols-5');
            $contenedorHistorialComerciante.remove();
            $contenedorHistorialProductor.remove();
            break;

        case 3:
            console.log('oeiueoi')
            if (
                location.pathname.indexOf(paths['historial']) === -1 &&
                location.pathname.indexOf(paths['informacion']) === -1) {
                    $contenedorBaseHtml.remove();
                }
            $btn.removeChild($btn.children[0]);
            $btn.removeChild($btn.children[0]);
            $btn.removeChild($btn.children[0]);
            $btn.children[0].querySelector('span').textContent += ' Compras';
            $btn.classList.add('grid-cols-3')
            $contenedorHistorialExterno.remove();
            $contenedorHistorialProductor.remove();
            break;

        case 4:
            if (location.pathname.indexOf(paths['publicacion']) === -1 &&
                location.pathname.indexOf(paths['historial']) === -1 &&
                location.pathname.indexOf(paths['informacion']) === -1 &&
                location.pathname.indexOf(paths['solicitud']) === -1) {
                $contenedorBaseHtml.remove();
            }
            $btn.removeChild($btn.children[1]);
            $btn.removeChild($btn.children[0]);
            $btn.children[1].querySelector('span').textContent += ' Publicaciones';
            $btn.classList.add('grid-cols-4')
            $contenedorHistorialComerciante.remove();
            $contenedorHistorialExterno.remove();
            break;

        default:
            $contenedorBaseHtml.remove();
            break;
    };
};
