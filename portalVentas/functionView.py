from math import trunc
from os import error
import sys
import time
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
import threading

from .functionSql import SP_SALDOS, VIEW_ORGANIZACION_TERRITORIAL
from .models import *
from django.db.models import Max
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login

today = datetime.now()
viewOrganizacionTerritorial = VIEW_ORGANIZACION_TERRITORIAL()
sys.setrecursionlimit(10**6) 

def idMaxMasUno(modelo, campo):
    id = modelo.objects.all().aggregate(Max(campo))['{}__max'.format(campo)]

    if id == None:
        id = 1 
    else:
        id = id + 1
    return id

def obtenerProductos():
    ventaNormal = []
    for obj in SP_SALDOS():
        days = (obj['FECHA_ESTIMADA_VENCIMIENTO'] - today).days
        if days > 3 and obj['N_REP_FRUTA'] == 1:
            ventaNormal.append(obj)
    return ventaNormal

def obtenerOfertas():
    oferta = []
    for obj in SP_SALDOS():
        days = (obj['FECHA_ESTIMADA_VENCIMIENTO'] - today).days
        if days <= 3 and obj['N_REP_FRUTA'] > 1:
            oferta.append(obj)
    return oferta

def obtenerProductoId(id):
    producto = []
    for obj in SP_SALDOS():
        if obj['ID_STOCK'] == id:
            producto = obj
            break;
    return producto

def obtenerProductoIdyNombre(id, nombreFruta):
    nombreFruta = nombreFruta.lower()
    producto = []
    arrNombreFruta = nombreFruta.replace('-', ' ').split(' ')
    especie = arrNombreFruta[0]
    variedad = nombreFruta.replace('{}-'.format(especie), '').replace('-', ' ')


    for obj in VIEW_LISTA_SOLICITUDES('O'):
        if obj['ID_SOLICITUD'] == id and obj['DES_ESPECIE'].lower().replace('á', 'a') == especie and obj['DES_VARIEDAD'].lower() == variedad:
            producto = obj
            break;
    return producto  

def obtenerUsuario(id):
    try:
        return Usuario.objects.get(id_usuario = id)
    except ObjectDoesNotExist:
        return False

def buscarRut(rut):
    try:
        Usuario.objects.get(run_usuario = rut)
        return True
    except ObjectDoesNotExist:
        return False

def buscarCorreo(correo):
    try:
        Usuario.objects.get(email = correo)
        return True
    except ObjectDoesNotExist:
        return False

def agregarUsuario(datosUsuario, rol, pais):
    # 0 = El rut {} ya existe.'.format(datosUsuario['REGISTRO_RUT']
    # 1 = El correo {} ya existe.'.format(datosUsuario['REGISTRO_CORREO']
    # 2 = Correcto
    if buscarRut(datosUsuario['REGISTRO_RUT']):
        return 0
    elif buscarCorreo(datosUsuario['REGISTRO_CORREO'].lower().strip()):
        return 1

    v_id_usuario = idMaxMasUno(Usuario, 'id_usuario')
    v_run_usuario = datosUsuario['REGISTRO_RUT']
    v_nombre = datosUsuario['REGISTRO_NOMBRE'].lower().strip()
    v_ap_paterno = datosUsuario['REGISTRO_PATERNO'].lower().strip()
    v_ap_materno = datosUsuario['REGISTRO_MATERNO'].lower().strip()
    v_fecha_nac = datetime.strptime(datosUsuario['REGISTRO_FECHA'], '%d/%m/%Y')
    v_email = datosUsuario['REGISTRO_CORREO'].lower().strip()
    v_direccion = datosUsuario['REGISTRO_DIRECCION'].lower().strip()
    v_num_celular = datosUsuario['REGISTRO_CELULAR']
    v_clave = datosUsuario['REGISTRO_CONTRASENIA1']
    v_id_estado = EstadoUsuario.objects.get(id_estado = 1)
    v_id_comuna = Comuna.objects.get(id_comuna = datosUsuario['REGISTRO_COMUNA']) 
    v_id_rol = Rol.objects.get(id_rol = rol) 
    v_id_pais = Pais.objects.get(id_pais = pais) 

    # USUARIO PARA LA DB
    Usuario.objects.create(
        id_usuario = v_id_usuario,
        run_usuario = v_run_usuario,
        nombre = v_nombre,
        ap_paterno = v_ap_paterno,
        ap_materno = v_ap_materno,
        fecha_nac = v_fecha_nac,
        email = v_email,
        direccion = v_direccion,
        num_celular = v_num_celular,
        clave = v_clave,
        id_estado = v_id_estado,
        id_comuna = v_id_comuna,
        id_rol = v_id_rol,
        id_pais = v_id_pais
    )

    # USUARIO PARA DJANGO
    for rolTabla in Rol.objects.all():
        if rolTabla.id_rol == rol:
            rolAsignado = rolTabla.des_rol

    usuarioDjango = User.objects.create_user(v_id_usuario, v_email, v_clave)
    usuarioDjango.first_name = v_nombre
    usuarioDjango.last_name = '{} {}'.format(v_ap_paterno, v_ap_materno)
    grupo = Group.objects.get(name='Comerciante') 
    grupo.user_set.add(usuarioDjango)
    usuarioDjango.save()

    return 2

def autentificarUsuario(solicitud, correo, contrasenia):
    try:
        usuario = User.objects.get(email = correo.lower().strip())
    except ObjectDoesNotExist:
        return 0
    
    usuarioAutenticado = authenticate(solicitud, username=usuario, password=contrasenia)
    if usuarioAutenticado is not None:
        login(solicitud, usuarioAutenticado)
        return 1
    else:
        return 2

def crearVentaLocal(objFruta, kilos_comprados, idUsuario):
    print(idUsuario)
    v_id_venta_local = idMaxMasUno(VentaLocal, 'id_venta_local')
    v_kilos_iniciales = VentaLocal.objects.filter(id_stock = objFruta['KILOS'])
    v_kilos_comprados = int(kilos_comprados)
    v_id_usuario = Usuario.objects.get(id_usuario = idUsuario)
    v_id_stock = StockSobrante.objects.get(id_stock = objFruta['ID_STOCK'])
    diffKilos = int(objFruta['KILOS']) - int(kilos_comprados)

    if str(v_kilos_iniciales) == '<QuerySet []>':
        v_kilos_iniciales = int(objFruta['KILOS'])
    else:
        v_kilos_iniciales = v_kilos_iniciales.order_by('-kilos_iniciales')[0].kilos_iniciales

    if diffKilos == 0 :
        estado = 2
    else:
        estado = 1

    v_id_estado = EstadoVenta.objects.get(id_estado = estado)

    actualizarStockSobrante(objFruta['ID_STOCK'], diffKilos, '-')

    VentaLocal.objects.create(
        id_venta_local = v_id_venta_local,
        kilos_iniciales = v_kilos_iniciales,
        kilos_comprados = v_kilos_comprados,
        id_usuario = v_id_usuario,
        id_stock = v_id_stock,
        id_estado = v_id_estado
    )

def actualizarStockSobrante(v_id_stock, v_kilos, operador):
    if operador == '-':
        StockSobrante.objects.filter(id_stock = v_id_stock).update(kilos = v_kilos)
    elif operador == '+':
        kilos_actuales = StockSobrante.objects.get(id_stock = v_id_stock).kilos 
        kilos_devueltos = kilos_actuales + v_kilos
        StockSobrante.objects.filter(id_stock = v_id_stock).update(kilos = kilos_devueltos)

def crearPago(datosPago):
    try:
        v_id_banco = Banco.objects.get(id_banco = int(datosPago['SELECT_BANCO'])).id_banco
        v_monto = int(datosPago['TOTAL_VENTA'].replace('.',''))
        v_fecha_pago = datetime.now().date()
        v_id_venta_local = VentaLocal.objects.only('id_venta_local').get(id_venta_local = datosPago['ID_VENTA_LOCAL']) if datosPago['ID_VENTA_LOCAL'] != None else datosPago['ID_VENTA_LOCAL']

        Pago.objects.create(
            id_pago = idMaxMasUno(Pago, 'id_pago'),
            id_banco = v_id_banco,
            monto = v_monto,
            fecha_pago = v_fecha_pago,
            id_venta_local = v_id_venta_local
        )

        return 1
    except Exception as e:
        print('='*120)
        print('crearPago - Msg del error : ' + str(e))
        print('='*120)
        return 0

def verificarPagos():
    query_venta_local = VentaLocal.objects.all()
    query_pago = Pago.objects.all()

    for row in query_venta_local:
        ventaConPago = query_pago.filter(id_venta_local = row.id_venta_local)
        if str(ventaConPago) == '<QuerySet []>': # Venta Sin Pago
            actualizarStockSobrante(row.id_stock.id_stock, row.kilos_comprados, '+')
            VentaLocal.objects.filter(id_venta_local = int(row.id_venta_local)).delete()

def crearSolicitud(datosSolicitud, usuario):
    v_id_solicitud = idMaxMasUno(Solicitud, 'id_solicitud')
    row = []
    for i in range(len(datosSolicitud['ID'])):
        row.append({
         'ID': datosSolicitud['ID'][i],
         'FRUTA': datosSolicitud['FRUTA'][i],
         'VARIEDAD': datosSolicitud['VARIEDAD'][i],
         'CANTIDAD': datosSolicitud['CANTIDAD'][i]
        })
    try:
        Solicitud.objects.create(
            id_solicitud = v_id_solicitud,
            fecha_creacion = today,
            id_usuario = Usuario.objects.get(id_usuario = int(usuario)),
            id_estado = EstadoSolicitud.objects.get(id_estado = 1)
        )
        for i in range(len(row)):
            DetalleSolicitud.objects.create(
                id_pedido = idMaxMasUno(DetalleSolicitud, 'id_pedido'),
                id_solicitud = Solicitud.objects.get(id_solicitud = v_id_solicitud),
                id_variedad = Variedad.objects.get(id_variedad = int(row[i]['VARIEDAD'])),
                kilos = int(row[i]['CANTIDAD'])
            )
        return 1
    except ValueError:
        return 0

def VIEW_LISTA_SOLICITUDES(filtro, id_usuario = 0):
    # S = SOLICITUD
    # P = PUBLICACION
    # O = OFERTAR
    # OC = ORDEN DE COMPRA
    viewListaSolicitudes = []
    query = ''
    if filtro != 'S' and filtro != 'P' and filtro != 'O' and filtro != 'OC':
        query = 'SELECT * FROM VIEW_LISTA_SOLICITUDES WHERE ID_USUARIO = {} ORDER BY ID_ESTADO, ID_SOLICITUD DESC'.format(filtro)
    elif filtro == 'S':
        query = 'SELECT * FROM VIEW_LISTA_SOLICITUDES WHERE ID_ESTADO = 1 ORDER BY ID_SOLICITUD DESC'
    elif filtro == 'P':
        query = 'SELECT * FROM VIEW_LISTA_SOLICITUDES WHERE ID_ESTADO = 2 ORDER BY ID_PUBLICACION ASC, ID_SOLICITUD DESC'
    elif filtro == 'O':
        query = 'SELECT * FROM VIEW_LISTA_SOLICITUDES WHERE ID_ESTADO = 2 AND ID_PUBLICACION = 1 AND KILOS_OBTE IS NULL ORDER BY PUB_HORA_INI'
    elif filtro == 'OC':
        query = 'SELECT * FROM VIEW_LISTA_SOLICITUDES WHERE ID_USUARIO = {} AND ID_PUBLICACION = 2 ORDER BY ID_SOLICITUD DESC'.format(id_usuario)
        # query = 'SELECT * FROM VIEW_LISTA_SOLICITUDES where rownum = 1 ORDER BY ID_SOLICITUD DESC'


    for obj in Solicitud.objects.raw(query):

        viewListaSolicitudes.append({
            'ID_SOLICITUD' : obj.id_solicitud,
            'FECHA_CREACION' : obj.fecha_creacion,
            'HORA_INI_PUBLICACION' : obj.pub_hora_ini,
            'HORA_FIN_PUBLICACION' : obj.pub_hora_fin,
            'DES_ESPECIE' : obj.des_especie,
            'DES_VARIEDAD' : obj.des_variedad,
            'KILOS' : int(obj.kilos),
            'KILOS_OBTENIDOS' : int(obj.kilos_obte) if obj.kilos_obte != None else '-',
            'ID_PEDIDO' : obj.id_pedido,
            'DES_ESTADO' : obj.id_estado.des_estado,
            'DES_PUBLICACION' : obj.id_publicacion.des_estado if obj.id_publicacion != None else obj.id_publicacion,
            'NOMBRE_USUARIO' : '{} {}'.format(obj.id_usuario.nombre, obj.id_usuario.ap_paterno),
            'PAIS_USUARIO' : obj.id_usuario.id_pais.descripcion
        })

    return viewListaSolicitudes

def crearOferta(objOferta):
    v_id_oferta = idMaxMasUno(OfertaProductor, 'id_oferta')
    v_id_solicitud = Solicitud.objects.get(id_solicitud = int(objOferta['ID_SOLICITUD'][0]))
    
    v_id_detalle_of = idMaxMasUno(DetalleOferta, 'id_detalle_of')
    v_fecha_oferta = today
    v_kilos_total = objOferta['CANTIDAD_OFERTAR'][0]
    v_precio_total = objOferta['PRECIO_VENTA'][0]
    v_fecha_cosecha = datetime.strptime(objOferta['FECHA_COSECHA'][0], '%d/%m/%Y')
    v_cerrada = 0
    v_id_variedad = Variedad.objects.get(des_variedad = objOferta['VARIEDAD'][0])
    v_id_usuario = Usuario.objects.get(id_usuario = int(objOferta['ID_USUARIO'][0]))
    v_id_pedido = DetalleSolicitud.objects.get(id_pedido = int(objOferta['ID_PEDIDO'][0]))

    try:
        OfertaProductor.objects.create(id_oferta = v_id_oferta, id_solicitud = v_id_solicitud)

        DetalleOferta.objects.create(
            id_detalle_of = v_id_detalle_of,
            fecha_oferta = v_fecha_oferta,
            kilos_total = v_kilos_total,
            precio_total = v_precio_total,
            fecha_cosecha = v_fecha_cosecha,
            cerrada = v_cerrada,
            id_oferta = OfertaProductor.objects.get(id_oferta = int(v_id_oferta)),
            id_variedad = v_id_variedad,
            id_usuario = v_id_usuario,
            id_pedido = v_id_pedido
        )
        return 1
    except ValueError:      
        return 0

def cargarUsuariosDesdeDB():
    arrIdsUsuario = []
    for idsUsuario in Usuario.objects.all():
        arrIdsUsuario.append(idsUsuario)

    for usuario in arrIdsUsuario:
        try:
            User.objects.get(username = usuario.id_usuario)
        except User.DoesNotExist:
            usuarioDjango = User.objects.create_user(usuario.id_usuario, usuario.email.lower().strip(), usuario.clave)
            usuarioDjango.first_name = usuario.nombre.lower().strip()
            usuarioDjango.last_name = '{} {}'.format(usuario.ap_paterno.lower().strip(), usuario.ap_materno.lower().strip())
            grupo = Group.objects.get(name=usuario.id_rol.des_rol) 
            grupo.user_set.add(usuarioDjango)
            usuarioDjango.save()

def actualizarPublicacionGanadora(datosOfertaGanadora):
    idDetalleOferta = datosOfertaGanadora.split(',')[0]
    idPedido = datosOfertaGanadora.split(',')[1]
    kilosOfertados = datosOfertaGanadora.split(',')[2]

    DetalleSolicitud.objects.filter(id_pedido = idPedido).update(kilos_obte = kilosOfertados)

    DetalleOferta.objects.filter(id_pedido = idPedido).update(cerrada = -1)
    DetalleOferta.objects.filter(id_detalle_of = idDetalleOferta).update(cerrada = 1)

def crearOrdenCompra(datosOrden):
    v_id_orden = idMaxMasUno(OrdenCompra, 'id_orden')
    v_id_solicitud = int(datosOrden.split('|')[0])
    v_costo = int(datosOrden.split('|')[1])
    v_id_usuario = int(datosOrden.split('|')[2])
    v_id_estado_orden = int(datosOrden.split('|')[3])

    try:
        OrdenCompra.objects.create(
            id_orden = v_id_orden,
            id_solicitud = Solicitud.objects.get(id_solicitud = v_id_solicitud),
            id_estado = EstadoPedido.objects.get(id_estado = v_id_estado_orden)
        )

        if crearCostos(v_id_orden, v_id_usuario, v_id_estado_orden, v_costo) == False:
            OrdenCompra.objects.filter(id_orden = v_id_orden).delete()
            error
        elif crearStockSobrante(v_id_orden, v_id_solicitud) == False:
            OrdenCompra.objects.filter(id_orden = v_id_orden).delete()
            Costos.objects.filter(id_costo = idMaxMasUno(Costos, 'id_costo')).delete()
            error
        elif v_id_estado_orden == 1:
            datosPago = {
                'ID_VENTA_LOCAL' : None,
                'TOTAL_VENTA' : str(v_costo),
                'SELECT_BANCO' : '-1'}
            
            crearPago(datosPago)

        return 1
    except Exception as e:
        print('='*120)
        print('crearOrdenCompra - Msg del error : ' + str(e))
        print('='*120)
        return 0

def crearCostos(idOrden, idUsuario, idEstadoOrden, costo):
    v_id_usuario = Usuario.objects.get(id_usuario = idUsuario)
    v_id_estado_orden = EstadoPedido.objects.get(id_estado = idEstadoOrden)
    v_valor = round(costo/1.6)
    v_id_orden = OrdenCompra.objects.get(id_orden = idOrden)

    datos_usuario = '{} - {} {} {}'.format(v_id_usuario.id_usuario, v_id_usuario.nombre.split(' ')[0].capitalize(), v_id_usuario.ap_paterno.capitalize(), v_id_usuario.ap_materno.capitalize())
    v_descripcion = 'Aprobada por: {}'.format(datos_usuario) if v_id_estado_orden.id_estado == 1 else 'Rechazada por: {}'.format(datos_usuario)

    try:
        Costos.objects.create(
            id_costo = idMaxMasUno(Costos, 'id_costo'),
            descripcion = v_descripcion,
            valor = v_valor,
            id_orden = v_id_orden
        )
        return True
    except Exception as e:
        print('='*120)
        print('crearCostos - Msg del error : ' + str(e))
        print('='*120)
        return 0

def crearStockSobrante(idOrden, idSolicitud):
    v_id_orden = OrdenCompra.objects.get(id_orden = idOrden)
    arrRowDetalleOferta = []
    arrKilos_sobrante = []
    for idOferta in OfertaProductor.objects.filter(id_solicitud = idSolicitud):
        for row in DetalleOferta.objects.filter(id_oferta = idOferta):
            arrRowDetalleOferta.append(
                {
                    'FECHA_COSECHA' : row.fecha_cosecha,
                    'KILOS_SOLI' : row.id_pedido.kilos,
                    'KILOS_OBTE' : row.id_pedido.kilos_obte,
                    'COSTO' : row.precio_total,
                    'ID_VARIEDAD' : row.id_variedad
                }
        )
    for obj in arrRowDetalleOferta:
        if v_id_orden.id_estado.id_estado == 4:
            arrKilos_sobrante.append( int(obj['KILOS_OBTE']) )
        else:
            arrKilos_sobrante.append( int(obj['KILOS_OBTE']) - int(obj['KILOS_SOLI']) )
    try:
        i = 0
        for obj in arrRowDetalleOferta:
            v_fecha_cosecha = obj['FECHA_COSECHA']
            v_precio_kilo = int(obj['COSTO'])
            v_id_variedad = obj['ID_VARIEDAD']
            if arrKilos_sobrante[i] > 0:
                StockSobrante.objects.create(
                    id_stock = idMaxMasUno(StockSobrante, 'id_stock'),
                    kilos = arrKilos_sobrante[i],
                    fecha_cosecha = v_fecha_cosecha,
                    fecha_estimada_vencimiento = v_fecha_cosecha + timedelta(days=7),
                    precio_kilo = round(v_precio_kilo / int(obj['KILOS_OBTE'])) * 1.5,
                    id_orden = v_id_orden,
                    id_variedad = v_id_variedad
                )
            i += 1

        return True
    except Exception as e:
        print('='*120)
        print('crearStockSobrante - Msg del error : ' + str(e))
        print('='*120)
        return 0

def puntajePrecioVenta(cantidadOfertada, precioVenta):
    return cantidadOfertada / precioVenta

def puntajeFechaCosecha(fechaConsecha):
    puntaje = 0;
    
    if fechaConsecha == (datetime.now().date() + timedelta(0)):
        puntaje = 6
    elif fechaConsecha >= (datetime.now().date() + timedelta(-2)):
        puntaje = 5
    elif fechaConsecha >= (datetime.now().date() + timedelta(-4)):
        puntaje = 3
    elif fechaConsecha >= (datetime.now().date() + timedelta(-7)):
        puntaje = 1
    else:
        puntaje = -3

    return puntaje

def puntajeCantidadOfertada(cantidadOfertada, cantidadSolicitada):
    puntaje = '';

    if cantidadOfertada >= trunc(cantidadSolicitada * 2):
        puntaje = 10
    elif cantidadOfertada >= trunc(cantidadSolicitada * 1.5):
        puntaje = 6
    elif cantidadOfertada >= trunc(cantidadSolicitada * 1.1):
        puntaje = 5
    elif cantidadOfertada >= trunc(cantidadSolicitada * 1.07):
        puntaje = 4
    elif cantidadOfertada >= trunc(cantidadSolicitada * 1.05):
        puntaje = 3
    elif cantidadOfertada >= trunc(cantidadSolicitada * 1.03):
        puntaje = 2
    elif cantidadOfertada == trunc(cantidadSolicitada):
        puntaje = 1
            
    return puntaje

def obtenerArrConPuntajes(arrTemp, row):
    v_puntajePrecioVenta = puntajePrecioVenta(row.kilos_obtenidos, row.precio_total)
    v_puntajeFechaCosecha = puntajeFechaCosecha(row.fecha_cosecha.date())
    v_puntajeCantidadOfertada = puntajeCantidadOfertada(row.kilos_obtenidos, row.kilos_solicitados)
    arrTemp.append(
        {'ID_PUBLICACION' : row.id_detalle_of, 'ID_PEDIDO' : row.id_pedido, 'KILOS_OBTENIDOS' : row.kilos_obtenidos,'PUNTAJE_TOTAL' : (v_puntajePrecioVenta + v_puntajeFechaCosecha + v_puntajeCantidadOfertada)}
    )
    return arrTemp

def publicacionGanadora():
    query = """
    SELECT
        SOLI.ID_SOLICITUD,
        DETA_SOLI.ID_PEDIDO,
        DETA_OFER.ID_DETALLE_OF,
        SOLI.PUB_HORA_FIN,
        DETA_SOLI.KILOS KILOS_SOLICITADOS,
        DETA_SOLI.KILOS_OBTE KILOS_CUANDO_SE_CIERRE,
        DETA_OFER.KILOS_TOTAL KILOS_OBTENIDOS,
        DETA_OFER.PRECIO_TOTAL,
        DETA_OFER.FECHA_COSECHA,
        DETA_OFER.CERRADA,
        ROW_NUMBER()OVER (PARTITION BY DETA_SOLI.ID_PEDIDO ORDER BY DETA_SOLI.ID_PEDIDO) AS N_REP_PEDIDO
    FROM
        SOLICITUD SOLI
            INNER JOIN DETALLE_SOLICITUD DETA_SOLI
                ON SOLI.ID_SOLICITUD = DETA_SOLI.ID_SOLICITUD
            INNER JOIN DETALLE_OFERTA DETA_OFER
                ON DETA_SOLI.ID_PEDIDO = DETA_OFER.ID_PEDIDO
    WHERE
        SOLI.ID_ESTADO = 2 AND SOLI.ID_PUBLICACION = 1 AND DETA_OFER.CERRADA = 0 -- SOLICITUD ACEPTADA Y PUBLICACION EN PROCESO Y LA OFERTA/PEDIDO NO ESTA CERRADO
    """
    id_pedido = Solicitud.objects.raw(query)[0].id_pedido
    n_rep_pedido = Solicitud.objects.raw(query)[0].n_rep_pedido
    arrTemp = []
    for row in Solicitud.objects.raw(query):
        if id_pedido == row.id_pedido:
            arrTemp = obtenerArrConPuntajes(arrTemp, row)
        else:
            id_pedido = row.id_pedido
            arrTemp = []
            arrTemp = obtenerArrConPuntajes(arrTemp, row)

        if n_rep_pedido < row.n_rep_pedido:
            objObtenerArrConPuntajesOrdenado = sorted(arrTemp, key=lambda obj : obj['PUNTAJE_TOTAL'], reverse=True)[0]
            datosOfertaGanadora = '{},{},{}'.format(objObtenerArrConPuntajesOrdenado['ID_PUBLICACION'],
                                                    objObtenerArrConPuntajesOrdenado['ID_PEDIDO'],
                                                    objObtenerArrConPuntajesOrdenado['KILOS_OBTENIDOS'])
            actualizarPublicacionGanadora(datosOfertaGanadora)

        else:
            n_rep_pedido = row.n_rep_pedido

def treadCadaUnSegundo(contador):
    contador += 1
    horaActual = datetime.now().hour if len(str(datetime.now().hour)) == 2 else '0{}'.format(datetime.now().hour)
    minutoActual = datetime.now().minute if len(str(datetime.now().minute)) == 2 else '0{}'.format(datetime.now().minute)

    for obj in Solicitud.objects.filter(id_estado = 2, id_publicacion = 1):
        horafin = obj.pub_hora_fin.split(':')[0]
        minutoFin = obj.pub_hora_fin.split(':')[1]
        if int(horaActual) == int(horafin) and int(minutoActual) == int(minutoFin):
            publicacionGanadora()
            
    if contador < 60*60:
        time.sleep(1)
        treadCadaUnSegundo(contador)
    else:
        return 0

def iniciarThread():
    t = threading.Thread(target=treadCadaUnSegundo, args=(1, ), daemon=True)
    t.start()
   
    
# print('*'*100)
# print();
# print('*'*100)