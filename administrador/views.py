from administrador.functionSql import VIEW_CANTIDAD_OC_RECHAZADAS, VIEW_CANTIDAD_PUBLICACIONES_X_ESTADO, VIEW_COSTOS_X_MES, VIEW_EXTERNO_ORDENES_RECHAZADAS, VIEW_FRUTAS_DONADAS, VIEW_GANANCIAS_X_MES, VIEW_PEDIDOS, VIEW_CANTIDAD_SOLICITUDES_PENDIENTES, VIEW_PREFERENCIAS_BANCO, VIEW_PRODUCTORES_OFERTAS_APROBADAS, VIEW_VENTA_LOCAL_EXTERNA
from portalVentas.functionView import VIEW_LISTA_SOLICITUDES
from .functionView import *
from django.shortcuts import render
# Create your views here.

def home(request):
    tituloPagina = 'Administracion'
    return render(request, 'administrador/base.html', { 'tituloPagina' : tituloPagina})

def solicitud(request):
    tituloPagina = 'Solicitudes'
    mensajeSolicitud = 0
    inputName = {
        'APRUEBO' : '',
        'RECHAZO' : '',
    }
    if request.method == 'POST':
        for key in inputName:
            inputName[key] = request.POST.get(key)
        mensajeSolicitud = actualizarEstadoSolicitud(inputName)
    return render(request, 'administrador/solicitud.html', { 'tituloPagina' : tituloPagina, 'viewListaSolicitudes' : VIEW_LISTA_SOLICITUDES('S'), 'mensajeSolicitud' : mensajeSolicitud })

def publicacion(request):
    tituloPagina = 'Publicaciones'
    mensajePublicacion = 0
    inputName = {
        'DATOS_SOLICITUDES' : ''
    }
    if request.method == 'POST':
        for key in inputName:
            inputName[key] = request.POST.get(key)
        mensajePublicacion = actualizarPublicacion(inputName)
    actualizarAutomaticaEstadoSolicitud()
    return render(request, 'administrador/publicacion.html', { 'tituloPagina' : tituloPagina, 'viewListaSolicitudes' : VIEW_LISTA_SOLICITUDES('P'), 'mensajePublicacion' : mensajePublicacion})

def ordenCompra(request):
    tituloPagina = 'Ordenes de Compra'
    mensajeOrdenCompra = 0

    if request.method == 'POST':
        mensajeOrdenCompra = actualizarordenCompra(request.POST.get('ID_ORDEN__FECHA__RECEPCION'))
    return render(request, 'administrador/ordenCompra.html', { 'tituloPagina' : tituloPagina, 'mensajeOrdenCompra' : mensajeOrdenCompra, 'view_pedidos' : VIEW_PEDIDOS() })

def estadisticas(request):
    tituloPagina = 'Estadisticas'
    return render(request, 'administrador/estadisticas.html', {
        'tituloPagina' : tituloPagina,
        'view_cantidad_solicitudes_pendientes' : VIEW_CANTIDAD_SOLICITUDES_PENDIENTES(),
        'view_cantidad_oc_rechazadas' : VIEW_CANTIDAD_OC_RECHAZADAS(),
        'view_cantidad_publicaciones_x_estado' : VIEW_CANTIDAD_PUBLICACIONES_X_ESTADO(),
        'view_ganancias_x_mes' : VIEW_GANANCIAS_X_MES(),
        'view_costos_x_mes' : VIEW_COSTOS_X_MES(),
        'view_frutas_donadas' : VIEW_FRUTAS_DONADAS(), 
        'view_preferencias_banco' : VIEW_PREFERENCIAS_BANCO(),
        'view_productores_ofertas_aprobadas' : VIEW_PRODUCTORES_OFERTAS_APROBADAS(),
        'view_externo_ordenes_rechazadas' : VIEW_EXTERNO_ORDENES_RECHAZADAS(),
        'view_venta_local_externa' : VIEW_VENTA_LOCAL_EXTERNA()})