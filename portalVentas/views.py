from portalVentas.functionSql import CARGAR_IMAGENES, VIEW_DATOS_COTIZACION, VIEW_FRUTAS, VIEW_HISTORIAL_COMERCIANTE, VIEW_HISTORIAL_EXTERNO, VIEW_HISTORIAL_PRODUCTOR, VIEW_OFERTAS_PRODUCTOR, VIEW_PEDIDOS_ACEPTADOS
from django.contrib import auth
from django.contrib.auth import logout
from portalVentas.models import OrdenCompra, VentaLocal
from django.shortcuts import render
from .functionView import VIEW_LISTA_SOLICITUDES, actualizarPublicacionGanadora, autentificarUsuario, cargarUsuariosDesdeDB, crearOferta, crearOrdenCompra, crearPago, crearSolicitud, idMaxMasUno, iniciarThread, obtenerProductoIdyNombre, obtenerUsuario, today, obtenerProductos, obtenerOfertas, verificarPagos, viewOrganizacionTerritorial, obtenerProductoId, crearVentaLocal, agregarUsuario

def home(request):
    tituloPagina = 'Inicio'
    cargarUsuariosDesdeDB()
    CARGAR_IMAGENES()
    usuario = obtenerUsuario(int('{}'.format(request.user))) if '{}'.format(request.user) != 'AnonymousUser' else 0
    pagoEfectuado = None
    if request.method == 'POST':
        inputName = {
            'ID_VENTA_LOCAL' : '',
            'TOTAL_VENTA' : '',
            'SELECT_BANCO' : ''}
        
        for key in inputName:
            inputName[key] = request.POST.get(key)
        pagoEfectuado = crearPago(inputName)
        verificarPagos()

    if request.GET.getlist('..') != []:
            logout(request)
    return render(request, 'portalVentas/index.html', 
    {'tituloPagina' : tituloPagina,
     'ventaNormal' : obtenerProductos(),
     'oferta' : obtenerOfertas(),
     'pagoEfectuado' : pagoEfectuado,
     'usuario' : usuario })

def informacionBestFruit(request):
    tituloPagina = 'Informacion Best Fruit'
    return render(request, 'portalVentas/informacionBestFruit.html', { 'tituloPagina' : tituloPagina })

def login(request):
    tituloPagina = 'Ingreso'
    mensajeLogin = None
    inputName = {
        'LOGIN_CORREO' : '',
        'LOGIN_PASS' : '',
    }
    
    if request.method == 'POST':
        for key in inputName:
            inputName[key] = request.POST.get(key)
        mensajeLogin = autentificarUsuario(request, inputName['LOGIN_CORREO'], inputName['LOGIN_PASS'])
    usuario = obtenerUsuario(int('{}'.format(request.user))) if '{}'.format(request.user) != 'AnonymousUser' else 0

    return render(request, 'portalVentas/login.html', { 'tituloPagina' : tituloPagina, 'mensajeLogin' : mensajeLogin, 'usuario' : usuario })

def registro(request):
    tituloPagina = 'Registro'
    mensajeRegistro = None
    inputName = {
        'REGISTRO_RUT' : '',
        'REGISTRO_PASAPORTE' : '',
        'REGISTRO_FECHA' : '',
        'REGISTRO_NOMBRE' : '',
        'REGISTRO_PATERNO' : '',
        'REGISTRO_MATERNO' : '',
        'REGISTRO_CORREO' : '',
        'REGISTRO_CELULAR' : '',
        'REGISTRO_DIRECCION' : '',
        'REGISTRO_REGION' : '',
        'REGISTRO_PROVINCIA' : '',
        'REGISTRO_COMUNA' : '',
        'REGISTRO_CONTRASENIA1' : ''
    }

    if request.method == 'POST':
        for key in inputName:
            inputName[key] = request.POST.get(key)
        mensajeRegistro = agregarUsuario(inputName, 3, 4)
        
        
    return render(request, 'portalVentas/registro.html', { 
        'tituloPagina' : tituloPagina,
        'fechaActual' : today,
        'viewOrganizacionTerritorial' : viewOrganizacionTerritorial,
        'mensajeRegistro' : mensajeRegistro
    })

def detalle(request, id):
    # SE AGREGA LA VARIABLE 'oferta' DADO QUE LA VISTA OFERTA.HTML NECESITA DE ESTA VARIABLE
    tituloPagina = '{} {}'.format(obtenerProductoId(id)['DES_ESPECIE'], obtenerProductoId(id)['DES_VARIEDAD'])
    verificarPagos()
    return render(request, 'portalVentas/detalle.html', { 'tituloPagina' : tituloPagina, 'fruta' : obtenerProductoId(id), 'oferta' : obtenerOfertas() })

def transbank(request, id):
    tituloPagina = 'Transbank'
    verificarPagos()
    inputName = {
        'DETALLE_INPUT_CANTIDAD' : '',
        'DETALLE_INPUT_TOTAL' : ''}
    
    if request.method == 'POST':
        for key in inputName:
            inputName[key] = request.POST.get(key)
    crearVentaLocal(obtenerProductoId(id), inputName['DETALLE_INPUT_CANTIDAD'], request.user.username)
    return render(request, 'portalVentas/transbank.html', { 'tituloPagina' : tituloPagina, 'inputName' : inputName, 'fruta' : obtenerProductoId(id), 'id_venta_local' : idMaxMasUno(VentaLocal, 'id_venta_local') - 1})

def solicitud(request):
    tituloPagina = 'Solicitudes'
    usuario = obtenerUsuario(int('{}'.format(request.user))) if request.user != None else 0
    mensajeSolicitud = None
    inputName = {
         'ID': [],
         'FRUTA': [],
         'VARIEDAD': [],
         'CANTIDAD': []
    }

    if request.method == 'POST':
        for key in inputName:
            inputName[key] = request.POST.getlist(key)
        mensajeSolicitud = crearSolicitud(inputName, request.user.username)
    
    return render(request, 'portalVentas/solicitud.html', { 
        'tituloPagina' : tituloPagina,
        'usuario' : usuario,
        'viewFrutas' : VIEW_FRUTAS(),
        'mensajeSolicitud' : mensajeSolicitud,
        'viewListaSolicitudes' : VIEW_LISTA_SOLICITUDES( request.user.username )
     })

def docPdf(request):
    tituloPagina = 'PDF'
    usuario = obtenerUsuario(int('{}'.format(request.user))) if request.user != None else 0
    return render(request, 'portalVentas/docPdf.html', { 'tituloPagina' : tituloPagina, 'usuario' : usuario,  })

def pedido(request):
    tituloPagina = 'Pedidos'
    usuario = obtenerUsuario(int('{}'.format(request.user))) if request.user != None else 0
    if request.method == "POST":
        crearOrdenCompra(request.POST.getlist('DATOS_ORDEN_COMPRA')[0])
    return render(request, 'portalVentas/pedido.html', {
    'tituloPagina' : tituloPagina,
    'usuario' : usuario,
    'viewDatosCotizacion' : VIEW_DATOS_COTIZACION(usuario.id_usuario),
    'view_pedidos_aceptados' : VIEW_PEDIDOS_ACEPTADOS()})

def historial(request):
    tituloPagina = 'Historial'
    usuario = obtenerUsuario(int('{}'.format(request.user))) if request.user != None else 0
    
    return render(request, 'portalVentas/historial.html', {
        'tituloPagina' : tituloPagina,
        'usuario' : usuario,
        'view_historial_comerciante' : VIEW_HISTORIAL_COMERCIANTE(usuario.id_usuario),
        'view_historial_externo' : VIEW_HISTORIAL_EXTERNO(usuario.id_usuario),
        'view_historial_productor' : VIEW_HISTORIAL_PRODUCTOR(usuario.id_usuario)})

def informacion(request):
    tituloPagina = 'Informacion'
    usuario = obtenerUsuario(int('{}'.format(request.user))) if request.user != None else 0
    return render(request,
    'portalVentas/informacion.html', { 'tituloPagina' : tituloPagina, 'usuario' : usuario, 'viewOrganizacionTerritorial' : viewOrganizacionTerritorial})

def publicacion(request):
    tituloPagina = 'Publicaciones'
    usuario = obtenerUsuario(int('{}'.format(request.user))) if request.user != None else 0
    
    return render(request, 'portalVentas/publicacion.html', { 'tituloPagina' : tituloPagina, 'usuario' : usuario, 'viewListaSolicitudes' : VIEW_LISTA_SOLICITUDES('O') })

def ofertarProducto(request, idSolicitud, idPedido, fruta):
    tituloPagina = 'Oferta Producto'
    usuario = obtenerUsuario(int('{}'.format(request.user))) if request.user != None else 0
    mensajeOfertarProducto = None
    inputName = {
        'CANTIDAD_OFERTAR' : '',
        'PRECIO_VENTA' : '',
        'FECHA_COSECHA' : '',
        'ID_SOLICITUD' : '',
        'VARIEDAD' : '',
        'ID_USUARIO' : '',
        'ID_PEDIDO' : ''
    }

    if request.method == 'POST':
        for key in inputName:
            inputName[key] = request.POST.getlist(key)
        mensajeOfertarProducto = crearOferta(inputName)
        
    return render(request, 'portalVentas/ofertarProducto.html', {
        'tituloPagina' : tituloPagina,
        'usuario' : usuario,
        'fruta' : obtenerProductoIdyNombre(idSolicitud, fruta),
        'mensajeOfertarProducto' : mensajeOfertarProducto,
        'view_ofertas_productor' : VIEW_OFERTAS_PRODUCTOR(idSolicitud, idPedido)})

iniciarThread()