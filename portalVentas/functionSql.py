from django.db import connection
import cx_Oracle
import sys

sys.path.append("C:/Users/leone/Downloads/Django/feriaVirtual")

usr = 'c##feriaVirtual'
passwd = 'feriavirtual'
# ("insert into SomeTable values (:1, :2)", (1, "Some string")) 
    # connection.commit()

def SP_SALDOS():
    with cx_Oracle.connect(usr, passwd, 'localhost:1521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        outVal = cursor.connection.cursor()
        cursor.callproc('SP_SALDOS', [outVal])
        sp_saldos = []
        for row in outVal.fetchall():
            sp_saldos.append({
                'ID_STOCK' : row[0],
                'ID_VENTA_LOCAL' : row[1],
                'FECHA_COSECHA' : row[2],
                'FECHA_ESTIMADA_VENCIMIENTO' : row[3],
                'DES_ESPECIE' : row[4],
                'DES_VARIEDAD' : row[5],
                'KILOS' : row[6],
                'PRECIO_KILO' : row[7],
                'DESC_IMAGEN' : row[8],
                'EXT_IMAGEN' : row[9],
                'IMAGEN' : "/media/variedad/{}.{}".format(row[8], row[9]),
                'ESTADO_VENTA' : row[11],
                'N_REP_FRUTA' : row[12]
            })
    return sp_saldos

def CARGAR_IMAGENES():
    with cx_Oracle.connect(usr, passwd, 'localhost:1521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        for row in cursor.execute('SELECT * FROM IMAGEN').fetchall():
            CARGAR_IMAGEN(row[3].read(), row[1].replace(' ', '-'), row[2])

def CARGAR_IMAGEN(imagenBlob ,nombreArchivo, extensionArchivo):
    leerImagenBlob = imagenBlob
    crearArchivo = open('media/variedad/{}.{}'.format(nombreArchivo, extensionArchivo), 'wb')
    llenarArchivo = crearArchivo.write(leerImagenBlob)
    crearArchivo.close()
    return crearArchivo

def VIEW_ORGANIZACION_TERRITORIAL():
    with cx_Oracle.connect(usr, passwd, 'localhost:1521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_organizacion_territorial = []

        for row in cursor.execute('SELECT * FROM REGION').fetchall():
            view_organizacion_territorial.append({
                "ID_REGION" : row[0],
                "DES_REGION" : '{}'.format(row[1])
            })
        for row in cursor.execute('SELECT * FROM PROVINCIA').fetchall():
            view_organizacion_territorial.append({
                "ID_PROVINCIA" : row[0],
                "DES_PROVINCIA" : '{}'.format(row[1]),
                "ID_REGION_PROVINCIA" : row[2]
            })
        for row in cursor.execute('SELECT * FROM COMUNA').fetchall():
            view_organizacion_territorial.append({
                "ID_COMUNA" : row[0],
                "DES_COMUNA" : '{}'.format(row[1]),
                "ID_PROVINCIA_COMUNA" : row[2]
            })

    return view_organizacion_territorial

def VIEW_FRUTAS():
    with cx_Oracle.connect(usr, passwd, 'localhost:1521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_frutas = []

        for row in cursor.execute('SELECT * FROM VARIEDAD').fetchall():
            view_frutas.append({
                "ID_VARIEDAD" : row[0],
                "DES_VARIEDAD" : '{}'.format(row[1]),
                # "DIAS_VENCIMIENTO" : '{}'.format(row[2]),
                "ID_ESPECIE_VARIEDAD" : row[3]
                # "ID_IMAGEN" : row[4]
            })
        for row in cursor.execute('SELECT * FROM ESPECIE').fetchall():
            view_frutas.append({
                "ID_ESPECIE" : row[0],
                "DES_ESPECIE" : '{}'.format(row[1]),
            })

    return view_frutas

def VIEW_OFERTAS_PRODUCTOR(idSolicitud, idPedido):
    with cx_Oracle.connect(usr, passwd, 'localhost:1521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_ofertas_productor = []
        for row in cursor.execute('SELECT * FROM VIEW_OFERTAS_PRODUCTOR WHERE ID_SOLICITUD = {} AND ID_PEDIDO = {}'.format(idSolicitud, idPedido)).fetchall():
            view_ofertas_productor.append({
                "ID_DETALLE_OF" : row[0],
                "KILOS_TOTAL" : row[1],
                "PRECIO_TOTAL" : row[2],
                "FECHA_COSECHA" : row[3],
                "CERRADA" : row[4],
                "ID_USUARIO" : row[5],
                "ID_OFERTA" : row[6],
                "ID_SOLICITUD" : row[7],
                "ID_PEDIDO" : row[8],
                "NOMBRE_USUARIO" : '{} {}'.format(row[9].split(' ')[0], row[9].split(' ')[len(row[9].split(' ')) - 1]) if len(row[9].split(' ')) > 2 else row[9]
            })

    return view_ofertas_productor

def VIEW_DATOS_COTIZACION(idUsuario):
    with cx_Oracle.connect(usr, passwd, 'localhost:1521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_datos_cotizacion = []
        for row in cursor.execute('SELECT * FROM VIEW_DATOS_COTIZACION WHERE ID_USUARIO = {} AND ID_ESTADO_PUBLICACION = 2 AND CERRADA = 1 ORDER BY ID_ESTADO_ORDEN DESC'.format(idUsuario)).fetchall():
            view_datos_cotizacion.append({
                "ID_DETALLE_OF" : row[0],
                "ID_SOLICITUD" : row[1],
                "PRECIO_TOTAL" : row[2],
                "FECHA_COSECHA" : row[3],
                "CERRADA" : row[4],
                "DES_ESPECIE" : row[5],
                "DES_VARIEDAD" : row[6],
                "ID_USUARIO" : row[7],
                "RUN_USUARIO" : row[8],
                "NOMBRE_USUARIO" : row[9],
                "DIRECCION" : row[10],
                "CORREO" : row[11],
                "ID_PEDIDO" : row[12],
                "KILOS" : row[13],
                "KILOS_OBTE" : row[14],
                "ID_ESTADO_ORDEN" : 0 if row[15] == None else row[15],
                "ID_ESTADO_PUBLICACION" : row[16]

            })
    return view_datos_cotizacion

def VIEW_PEDIDOS_ACEPTADOS():
    with cx_Oracle.connect(usr, passwd, 'localhost:1521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_pedidos_aceptados = []
        for row in cursor.execute('SELECT * FROM VIEW_PEDIDOS_ACEPTADOS WHERE ID_ESTADO_PEDIDO <> 4 ORDER BY FECHA_RECEPCION, ID_ORDEN DESC').fetchall():
            view_pedidos_aceptados.append({
                "ID_ORDEN" : row[0],
                "FECHA_RECEPCION" : '-' if row[1] == None else row[1],
                "ID_SOLICITUD" : row[2],
                "ID_ESTADO_PEDIDO" : row[3],
                "DESC_ESTADO" : row[4]
            })
    return view_pedidos_aceptados
    

    
    # A = """

def VIEW_HISTORIAL_COMERCIANTE(idUsuario):
    with cx_Oracle.connect(usr, passwd, 'localhost:1521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_historial_comerciante = []
        for row in cursor.execute('SELECT * FROM VIEW_HISTORIAL_COMERCIANTE WHERE ID_USUARIO = {}'.format(idUsuario)).fetchall():
            view_historial_comerciante.append({
                "N_VENTA" : row[0],
                "FECHA_COMPRA" : row[1],
                "FRUTA" : row[2],
                "KILOS_COMPRADOS" : row[3],
                "MONTO" : row[4]
            })

    return view_historial_comerciante
    
def VIEW_HISTORIAL_EXTERNO(idUsuario):
    with cx_Oracle.connect(usr, passwd, 'localhost:1521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_historial_externo = []
        for row in cursor.execute('SELECT * FROM VIEW_HISTORIAL_EXTERNO WHERE ID_USUARIO = {}'.format(idUsuario)).fetchall():
            view_historial_externo.append({
                "N_VENTA" : row[0],
                "FECHA_RECEPCION" : row[1],
                "FRUTA" : row[2],
                "KILOS_SOLICITADOS" : row[3],
                "MONTO" : row[4],
                "ESTADO" : row[5],
                "N_REP_SOLICITUD" : row[6]
            })

    return view_historial_externo

def VIEW_HISTORIAL_PRODUCTOR(idUsuario):
    with cx_Oracle.connect(usr, passwd, 'localhost:1521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_historial_productor = []
        for row in cursor.execute('SELECT * FROM VIEW_HISTORIAL_PRODUCTOR WHERE ID_USUARIO = {}'.format(idUsuario)).fetchall():
            view_historial_productor.append({
                "N_OFERTA" : row[0],
                "ID_PEDIDO" : row[1],
                "FECHA_OFERTA" : row[2],
                "FRUTA" : row[3],
                "KILOS_VENDIDOS" : row[4],
                "PRECIO_TOTAL" : row[5],
                "CERRADA" : row[6],
                "N_REP_OFERTA" : row[7]
            })

    return view_historial_productor