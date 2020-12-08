import cx_Oracle
import sys

sys.path.append("C:/Users/leone/Downloads/Django/feriaVirtual")

usr = 'admin_django'
passwd = 'admin1234'

def VIEW_PEDIDOS():
    with cx_Oracle.connect(usr, passwd, 'localhost:51521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_pedidos = []
        for row in cursor.execute('SELECT * FROM VIEW_PEDIDOS_ACEPTADOS').fetchall():
            view_pedidos.append({
                "ID_ORDEN" : row[0],
                "FECHA_RECEPCION" : '-' if row[1] == None else row[1],
                "ID_SOLICITUD" : row[2],
                "ID_ESTADO_PEDIDO" : row[3],
                "DESC_ESTADO" : row[4]
            })
    return view_pedidos
    
def VIEW_CANTIDAD_SOLICITUDES_PENDIENTES():
    with cx_Oracle.connect(usr, passwd, 'localhost:51521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_cantidad_solicitudes_pendientes = 0
        for row in cursor.execute('SELECT * FROM VIEW_CANTIDAD_SOLICITUDES_PENDIENTES').fetchall():
            view_cantidad_solicitudes_pendientes = row[1]

    return view_cantidad_solicitudes_pendientes

def VIEW_CANTIDAD_PUBLICACIONES_X_ESTADO():
    with cx_Oracle.connect(usr, passwd, 'localhost:51521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_cantidad_publicaciones_x_estado = {}
        for row in cursor.execute('SELECT * FROM VIEW_CANTIDAD_PUBLICACIONES_X_ESTADO ORDER BY ID_ESTADO').fetchall():
            view_cantidad_publicaciones_x_estado[row[1].upper().replace(' ', '_')] = row[2]

    return view_cantidad_publicaciones_x_estado

def VIEW_CANTIDAD_OC_RECHAZADAS():
    with cx_Oracle.connect(usr, passwd, 'localhost:51521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_cantidad_oc_rechazadas = 0
        for row in cursor.execute('SELECT * FROM VIEW_CANTIDAD_OC_RECHAZADAS').fetchall():
            view_cantidad_oc_rechazadas = row[1]

    return view_cantidad_oc_rechazadas

def VIEW_GANANCIAS_X_MES():
    with cx_Oracle.connect(usr, passwd, 'localhost:51521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_ganancias_x_mes = {}
        for row in cursor.execute('SELECT * FROM VIEW_GANANCIAS_X_MES ORDER BY N_MES').fetchall():
            view_ganancias_x_mes[row[0]] = row[1] if row[1] != None else 0
        
    return view_ganancias_x_mes

def VIEW_COSTOS_X_MES():
    with cx_Oracle.connect(usr, passwd, 'localhost:51521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_costos_x_mes = {}
        for row in cursor.execute('SELECT * FROM VIEW_COSTOS_X_MES ORDER BY N_MES').fetchall():
            view_costos_x_mes[row[0]] = row[1] if row[1] != None else 0
        
    return view_costos_x_mes

def VIEW_FRUTAS_DONADAS():
    with cx_Oracle.connect(usr, passwd, 'localhost:51521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_frutas_donadas = {}
        for row in cursor.execute('SELECT * FROM VIEW_FRUTAS_DONADAS ORDER BY KILOS_DONADOS').fetchall():
            view_frutas_donadas['{} {}'.format(row[0],row[1])] = row[2]
    return view_frutas_donadas

def VIEW_PREFERENCIAS_BANCO():
    with cx_Oracle.connect(usr, passwd, 'localhost:51521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_preferencias_banco = {}
        for row in cursor.execute('SELECT * FROM VIEW_PREFERENCIAS_BANCO ORDER BY CANTIDAD_USADO').fetchall():
            view_preferencias_banco[row[0]] = row[1]
    return view_preferencias_banco

def VIEW_PRODUCTORES_OFERTAS_APROBADAS():
    with cx_Oracle.connect(usr, passwd, 'localhost:51521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_productores_ofertas_aprobadas = {}
        for row in cursor.execute('SELECT * FROM VIEW_PRODUCTORES_OFERTAS_APROBADAS ORDER BY CANTIDAD_OFERTAS_APROBADAS').fetchall():
            view_productores_ofertas_aprobadas[row[0]] = row[1]
    return view_productores_ofertas_aprobadas

def VIEW_EXTERNO_ORDENES_RECHAZADAS():
    with cx_Oracle.connect(usr, passwd, 'localhost:51521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_externo_ordenes_rechazadas = {}
        for row in cursor.execute('SELECT * FROM VIEW_EXTERNO_ORDENES_RECHAZADAS ORDER BY CANTIDAD_ORDENES_RECHAZADAS').fetchall():
            view_externo_ordenes_rechazadas[row[0]] = row[1]
    return view_externo_ordenes_rechazadas

def VIEW_VENTA_LOCAL_EXTERNA():
    with cx_Oracle.connect(usr, passwd, 'localhost:51521/xe', encoding="UTF-8") as connection:
        cursor = connection.cursor()
        view_venta_local_externa = {}
        for row in cursor.execute('SELECT * FROM VIEW_VENTA_LOCAL_EXTERNA ORDER BY N_MES').fetchall():
            view_venta_local_externa[row[0]] = [row[1] if row[1] != None else 0, row[2] if row[2] != None else 0]
    return view_venta_local_externa