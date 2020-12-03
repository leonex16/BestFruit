from datetime import datetime
from portalVentas.functionView import VIEW_LISTA_SOLICITUDES
from portalVentas.models import *

def actualizarAutomaticaEstadoSolicitud():
    viewListaSolicitudes = VIEW_LISTA_SOLICITUDES('P')
    if len(viewListaSolicitudes) > 0:
        arrTemp = [[]]
        idAnterior = viewListaSolicitudes[0]['ID_SOLICITUD']
        indxArr = 0
        contadorPedidosCompletados = 0
        for indx in range( len(viewListaSolicitudes) ):
            
            if idAnterior == viewListaSolicitudes[indx]['ID_SOLICITUD']:
                arrTemp[indxArr].append(viewListaSolicitudes[indx])
            else:
                indxArr += 1
                arrTemp.append([])
                arrTemp[indxArr].append(viewListaSolicitudes[indx])
                idAnterior = viewListaSolicitudes[indx]['ID_SOLICITUD']

        for obj in arrTemp:

            for row in obj:
                if row['KILOS_OBTENIDOS'] != '-':
                    contadorPedidosCompletados += 1
            
            if contadorPedidosCompletados == len(obj):
                Solicitud.objects.filter(id_solicitud = int(obj[0]['ID_SOLICITUD'])).update(id_publicacion = EstadoPublicacion.objects.get(id_estado = 2))

            contadorPedidosCompletados = 0

def actualizarEstadoSolicitud(arrIdSol):
    arrIdSol = arrIdSol
    for key in arrIdSol:
        for val in arrIdSol[key].split('|'):
            if key == 'APRUEBO' and len(arrIdSol[key]) > 0:
                Solicitud.objects.filter(id_solicitud = int(val)).update(id_estado = EstadoSolicitud.objects.get(id_estado = 2))
                Solicitud.objects.filter(id_solicitud = int(val)).update(id_publicacion = EstadoPublicacion.objects.get(id_estado = 0))
            elif len(arrIdSol[key]) > 0:
                Solicitud.objects.filter(id_solicitud = int(val)).update(id_estado = EstadoSolicitud.objects.get(id_estado = 3))
                Solicitud.objects.filter(id_solicitud = int(val)).update(id_publicacion = EstadoPublicacion.objects.get(id_estado = 0))
    return 1
   
def actualizarPublicacion(arrDatosSol):
    arrTemp = arrDatosSol['DATOS_SOLICITUDES'].split('|')
    for idx in arrTemp:
        Solicitud.objects.filter(id_solicitud = int(idx.split(',')[0])).update(pub_hora_ini = idx.split(',')[1])
        Solicitud.objects.filter(id_solicitud = int(idx.split(',')[0])).update(pub_hora_fin = idx.split(',')[2])
        Solicitud.objects.filter(id_solicitud = int(idx.split(',')[0])).update(id_publicacion = EstadoPublicacion.objects.get(id_estado = 1))
    return 1

def actualizarordenCompra(arrDatosOrden):
    v_id_orden = int(arrDatosOrden.split(',')[0])
    v_fecha_recepcion = datetime.strptime(arrDatosOrden.split(',')[1], '%d/%m/%Y')
    try:
        OrdenCompra.objects.filter(id_orden = v_id_orden).update(fecha_recepcion = v_fecha_recepcion);
        OrdenCompra.objects.filter(id_orden = v_id_orden).update(id_estado = EstadoPedido.objects.get(id_estado = 3))
        return 1
    except Exception as e:
        print('='*120)
        print('actualizarordenCompra - Msg del error : ' + str(e))
        print('='*120)
        return 0
