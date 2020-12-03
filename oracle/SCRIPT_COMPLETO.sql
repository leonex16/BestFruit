DROP TABLE banco CASCADE CONSTRAINTS;

DROP TABLE calidad CASCADE CONSTRAINTS;

DROP TABLE calificacion CASCADE CONSTRAINTS;

DROP TABLE comuna CASCADE CONSTRAINTS;

DROP TABLE contrato CASCADE CONSTRAINTS;

DROP TABLE costos CASCADE CONSTRAINTS;

DROP TABLE detalle_oferta CASCADE CONSTRAINTS;

DROP TABLE detalle_solicitud CASCADE CONSTRAINTS;

DROP TABLE especie CASCADE CONSTRAINTS;

DROP TABLE estado_contrato CASCADE CONSTRAINTS;

DROP TABLE estado_pedido CASCADE CONSTRAINTS;

DROP TABLE estado_publicacion CASCADE CONSTRAINTS;

DROP TABLE estado_solicitud CASCADE CONSTRAINTS;

DROP TABLE estado_usuario CASCADE CONSTRAINTS;

DROP TABLE estado_venta CASCADE CONSTRAINTS;

DROP TABLE imagen CASCADE CONSTRAINTS;

DROP TABLE oferta_productor CASCADE CONSTRAINTS;

DROP TABLE orden_compra CASCADE CONSTRAINTS;

DROP TABLE pago CASCADE CONSTRAINTS;

DROP TABLE pais CASCADE CONSTRAINTS;

DROP TABLE provincia CASCADE CONSTRAINTS;

DROP TABLE puntos CASCADE CONSTRAINTS;

DROP TABLE region CASCADE CONSTRAINTS;

DROP TABLE rol CASCADE CONSTRAINTS;

DROP TABLE solicitud CASCADE CONSTRAINTS;

DROP TABLE stock_sobrante CASCADE CONSTRAINTS;

DROP TABLE usuario CASCADE CONSTRAINTS;

DROP TABLE variedad CASCADE CONSTRAINTS;

DROP TABLE venta_local CASCADE CONSTRAINTS;

CREATE TABLE banco (
    id_banco  NUMBER(3) NOT NULL PRIMARY KEY,
    des_banco VARCHAR2(30 CHAR) NOT NULL
);

CREATE TABLE calidad (
    id_calidad  NUMBER(1) NOT NULL PRIMARY KEY,
    detalle     VARCHAR2(20 CHAR) NOT NULL
);

CREATE TABLE especie (
    id_especie   NUMBER(3) NOT NULL PRIMARY KEY,
    des_especie  VARCHAR2(50 CHAR) NOT NULL
);

CREATE TABLE estado_contrato (
    id_estado   NUMBER(10) NOT NULL PRIMARY KEY,
    des_estado  VARCHAR2(50 CHAR) NOT NULL
);

CREATE TABLE estado_pedido (
    id_estado    NUMBER(1) NOT NULL PRIMARY KEY,
    desc_estado  VARCHAR2(20 CHAR) NOT NULL
);

CREATE TABLE estado_publicacion (
    id_estado   NUMBER(1) NOT NULL PRIMARY KEY,
    des_estado  VARCHAR2(50) NOT NULL
);

CREATE TABLE estado_solicitud (
    id_estado   NUMBER(1) NOT NULL PRIMARY KEY,
    des_estado  VARCHAR2(50) NOT NULL
);

CREATE TABLE estado_usuario (
    id_estado   NUMBER(5) NOT NULL PRIMARY KEY,
    des_estado  VARCHAR2(50 CHAR) NOT NULL
);

CREATE TABLE estado_venta (
    id_estado   NUMBER(1) NOT NULL PRIMARY KEY,
    des_estado  VARCHAR2(20 CHAR)
);

CREATE TABLE imagen (
    id_imagen   NUMBER(10) NOT NULL PRIMARY KEY,
    desc_imagen VARCHAR2(100) NOT NULL,
    ext_imagen  VARCHAR2(6) NOT NULL,
    imagen      BLOB
);

CREATE TABLE variedad (
    id_variedad      NUMBER(5) NOT NULL PRIMARY KEY,
    des_variedad     VARCHAR2(50 CHAR) NOT NULL,
    dias_vencimiento NUMBER (4) NOT NULL,
    id_especie       NUMBER(3) NOT NULL, -- FK
    id_imagen        NUMBER(10) NULL -- FK
);

CREATE TABLE pais (
    id_pais      NUMBER(10) NOT NULL PRIMARY KEY,
    descripcion  VARCHAR2(30)
);

CREATE TABLE region (
    id_region   NUMBER(3) NOT NULL PRIMARY KEY,
    des_region  VARCHAR2(50 CHAR) NOT NULL
);

CREATE TABLE rol (
    id_rol   NUMBER(1) NOT NULL PRIMARY KEY,
    des_rol  VARCHAR2(50) NOT NULL
);

CREATE TABLE provincia (
    id_provincia   NUMBER(3) NOT NULL PRIMARY KEY,
    des_provincia  VARCHAR2(50 CHAR) NOT NULL,
    id_region      NUMBER(3) NOT NULL -- FK
);

CREATE TABLE comuna (
    id_comuna     NUMBER(3) NOT NULL PRIMARY KEY,
    des_comuna    VARCHAR2(50) NOT NULL,
    id_provincia  NUMBER(3) NOT NULL -- FK
);

CREATE TABLE usuario (
    id_usuario   NUMBER(10) NOT NULL PRIMARY KEY,
    run_usuario  VARCHAR2(30 CHAR) NOT NULL UNIQUE,
    nombre       VARCHAR2(50 CHAR) NOT NULL,
    ap_paterno   VARCHAR2(25 CHAR) NOT NULL,
    ap_materno   VARCHAR2(25 CHAR) NOT NULL,
    fecha_nac    DATE NOT NULL,
    email        VARCHAR2(250 CHAR) NOT NULL UNIQUE,
    direccion    VARCHAR2(150 CHAR) NOT NULL,
    num_celular  NUMBER(9) NOT NULL,
    clave        VARCHAR2(255 CHAR) NOT NULL,
    id_estado    NUMBER(5) NOT NULL, -- FK
    id_comuna    NUMBER(3), -- FK
    id_rol       NUMBER(1) NOT NULL, -- FK
    id_pais      NUMBER(10) -- FK
);

CREATE TABLE calificacion (
    id_calificacion   NUMBER(1) NOT NULL PRIMARY KEY,
    des_calificacion  VARCHAR2(50) NOT NULL,
    id_usuario        NUMBER(10) -- FK
);

CREATE TABLE puntos (
    id_puntos   NUMBER(1) NOT NULL PRIMARY KEY,
    des_puntos  VARCHAR2(50 CHAR) NOT NULL,
    id_usuario  NUMBER(10) -- FK
);

CREATE TABLE solicitud (
    id_solicitud        NUMBER(10) NOT NULL PRIMARY KEY,
    fecha_creacion      DATE NOT NULL,
    pub_hora_ini        VARCHAR2(6),
    pub_hora_fin        VARCHAR2(6),
    id_usuario          NUMBER(10) NOT NULL, -- FK
    id_estado           NUMBER(1), -- FK
    id_publicacion      NUMBER(1) -- FK 
);

CREATE TABLE detalle_solicitud (
    id_pedido     NUMBER(10) NOT NULL PRIMARY KEY,
    id_solicitud  NUMBER(10) NOT NULL, -- FK
    id_variedad   NUMBER(3) NOT NULL, -- FK
    kilos         NUMBER(14) NOT NULL,
    kilos_obte    NUMBER(14) DEFAULT 0
);

CREATE TABLE orden_compra (
    id_orden            NUMBER(10) NOT NULL PRIMARY KEY,
    fecha_recepcion     DATE,
    id_solicitud        NUMBER(10) NOT NULL, -- FK
    id_estado           NUMBER(1) -- FK
);

CREATE TABLE costos (
    id_costo     NUMBER(10) NOT NULL PRIMARY KEY,
    descripcion  VARCHAR2(150) NOT NULL,
    valor        NUMBER(10),
    id_orden     NUMBER(10) -- FK
);

CREATE TABLE oferta_productor (
    id_oferta              NUMBER(10) NOT NULL PRIMARY KEY,
    id_solicitud            NUMBER(10) NOT NULL -- FK
);

CREATE TABLE detalle_oferta (
    id_detalle_of           NUMBER(10) NOT NULL PRIMARY KEY,
    fecha_oferta            DATE NOT NULL,
    kilos_total             NUMBER(10) NOT NULL,
    precio_total            NUMBER(10) NOT NULL,
    fecha_cosecha           DATE NOT NULL,
    cerrada                 NUMBER(1) DEFAULT 0 NOT NULL,
    id_oferta               NUMBER(10) NOT NULL, -- FK
    id_variedad		        NUMBER(3) NOT NULL, -- FK
    id_usuario              NUMBER(10) NOT NULL, -- FK
    id_pedido               NUMBER(10) NOT NULL -- FK
);

CREATE TABLE contrato (
    id_contrato    NUMBER(10) NOT NULL PRIMARY KEY,
    fecha_inicio   DATE NOT NULL,
    fecha_termino  DATE NOT NULL,
    vigencia       CHAR(1) NOT NULL,
    id_usuario     NUMBER(10), -- FK
    id_estado      NUMBER(10) NOT NULL -- FK
);

CREATE TABLE venta_local (
    id_venta_local  NUMBER(10) NOT NULL PRIMARY KEY,
    kilos_iniciales NUMBER(10)NOT NULL,
    kilos_comprados NUMBER(10)NOT NULL,
    id_usuario      NUMBER(10) NOT NULL, -- FK
    id_stock        NUMBER(10) NOT NULL, -- FK
    id_estado       NUMBER(1) NOT NULL  -- FK
);

CREATE TABLE pago (
    id_pago         NUMBER(10) NOT NULL PRIMARY KEY,
    monto           NUMBER(10),
    fecha_pago      DATE, -- Se agerga fecha para registrar cuanbdo se realiza el pago
    id_venta_local  NUMBER(10) NULL, -- FK
    id_banco        NUMBER(10) NOT NULL -- FK
);

CREATE TABLE stock_sobrante (
    id_stock                        NUMBER(10) NOT NULL PRIMARY KEY,
    kilos                           NUMBER(10),
    fecha_cosecha                   DATE,
    fecha_estimada_vencimiento      DATE,
    precio_kilo                     NUMBER(5),
    id_orden                        NUMBER(10), -- FK
    id_variedad          			NUMBER(5) NOT NULL -- FK
);

ALTER TABLE calificacion
    ADD CONSTRAINT calificacion_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id_usuario );

ALTER TABLE orden_compra
    ADD CONSTRAINT orden_compra_estado_fk FOREIGN KEY ( id_estado )
        REFERENCES estado_pedido ( id_estado );

ALTER TABLE comuna
    ADD CONSTRAINT comuna_provincia_fk FOREIGN KEY ( id_provincia )
        REFERENCES provincia ( id_provincia );

ALTER TABLE contrato
    ADD CONSTRAINT contrato_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id_usuario );

ALTER TABLE costos
    ADD CONSTRAINT costos_orden_fk FOREIGN KEY ( id_orden )
        REFERENCES orden_compra ( id_orden );

ALTER TABLE detalle_oferta
    ADD CONSTRAINT id_variedad_fk FOREIGN KEY ( id_variedad )
        REFERENCES variedad ( id_variedad );

ALTER TABLE detalle_oferta
    ADD CONSTRAINT detalle_ofertar_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id_usuario );

ALTER TABLE detalle_oferta
    ADD CONSTRAINT detalle_ofertar_pedido_fk FOREIGN KEY ( id_pedido )
        REFERENCES detalle_solicitud ( id_pedido );

ALTER TABLE detalle_oferta
    ADD CONSTRAINT detalle_ofertafk FOREIGN KEY ( id_oferta )
        REFERENCES oferta_productor ( id_oferta );

ALTER TABLE detalle_solicitud
    ADD CONSTRAINT deta_sol_id_variedad_fk FOREIGN KEY ( id_variedad )
        REFERENCES variedad ( id_variedad );

ALTER TABLE detalle_solicitud
    ADD CONSTRAINT detalle_solicitud_fk FOREIGN KEY ( id_solicitud )
        REFERENCES solicitud ( id_solicitud );

ALTER TABLE variedad
    ADD CONSTRAINT especie_variedad_fk FOREIGN KEY ( id_especie )
        REFERENCES especie ( id_especie );

ALTER TABLE contrato
    ADD CONSTRAINT estado_contrato_fk FOREIGN KEY ( id_estado )
        REFERENCES estado_contrato ( id_estado );

ALTER TABLE variedad
    ADD CONSTRAINT imagen_variedad_fk FOREIGN KEY ( id_imagen )
        REFERENCES imagen ( id_imagen ); 

ALTER TABLE oferta_productor
    ADD CONSTRAINT oferta_productor_solicitud_fk FOREIGN KEY ( id_solicitud )
        REFERENCES solicitud ( id_solicitud );

ALTER TABLE orden_compra
    ADD CONSTRAINT orden_compra_solicitud_fk FOREIGN KEY ( id_solicitud )
        REFERENCES solicitud ( id_solicitud );

ALTER TABLE pago
    ADD CONSTRAINT pago_venta_local_fk FOREIGN KEY ( id_venta_local )
        REFERENCES venta_local ( id_venta_local );

ALTER TABLE pago
    ADD CONSTRAINT pago_banco_fk FOREIGN KEY ( id_banco )
        REFERENCES banco ( id_banco );

ALTER TABLE provincia
    ADD CONSTRAINT provincia_region_fk FOREIGN KEY ( id_region )
        REFERENCES region ( id_region );

ALTER TABLE puntos
    ADD CONSTRAINT puntos_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id_usuario );

ALTER TABLE solicitud
    ADD CONSTRAINT solicitud_estado_publicacion_fk FOREIGN KEY ( id_publicacion )
        REFERENCES estado_publicacion ( id_estado );

ALTER TABLE solicitud
    ADD CONSTRAINT solicitud_estado_fk FOREIGN KEY ( id_estado )
        REFERENCES estado_solicitud ( id_estado );

ALTER TABLE solicitud
    ADD CONSTRAINT solicitud_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id_usuario );

ALTER TABLE venta_local
    ADD CONSTRAINT vent_loca_id_stock_fk FOREIGN KEY ( id_stock )
        REFERENCES stock_sobrante ( id_stock );

ALTER TABLE stock_sobrante
    ADD CONSTRAINT stock_sobrante_variedad_fk FOREIGN KEY ( id_variedad )
        REFERENCES variedad ( id_variedad );

ALTER TABLE stock_sobrante
    ADD CONSTRAINT stock_sobrante_orden_compra_fk FOREIGN KEY ( id_orden )
        REFERENCES orden_compra ( id_orden );

ALTER TABLE usuario
    ADD CONSTRAINT usuario_comuna_fk FOREIGN KEY ( id_comuna )
        REFERENCES comuna ( id_comuna );

ALTER TABLE usuario
    ADD CONSTRAINT estado_usuario_fk FOREIGN KEY ( id_estado )
        REFERENCES estado_usuario ( id_estado );

ALTER TABLE usuario
    ADD CONSTRAINT usuario_pais_fk FOREIGN KEY ( id_pais )
        REFERENCES pais ( id_pais );

ALTER TABLE usuario
    ADD CONSTRAINT usuario_rol_fk FOREIGN KEY ( id_rol )
        REFERENCES rol ( id_rol );

ALTER TABLE venta_local
    ADD CONSTRAINT venta_local_estado_venta_fk FOREIGN KEY ( id_estado )
        REFERENCES estado_venta ( id_estado );

ALTER TABLE venta_local
    ADD CONSTRAINT venta_local_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id_usuario );

COMMIT;

/

/

CREATE OR REPLACE PROCEDURE SP_SALDOS(SP_SALDOS OUT SYS_REFCURSOR) IS
    BEGIN
    OPEN SP_SALDOS FOR 
        SELECT
            STOCK.ID_STOCK,
            VENTA.ID_VENTA_LOCAL,
            STOCK.FECHA_COSECHA,
            STOCK.FECHA_ESTIMADA_VENCIMIENTO,
            ESPECIE.DES_ESPECIE,
            VARIEDAD.DES_VARIEDAD,
            STOCK.KILOS,
            STOCK.PRECIO_KILO,
            REPLACE(IMAGEN.DESC_IMAGEN, ' ', '-'),
            IMAGEN.EXT_IMAGEN,
            IMAGEN.IMAGEN AS IMAGEN,
            CASE
                WHEN VENTA.ID_ESTADO IS NULL THEN 1
                ELSE VENTA.ID_ESTADO
            END AS ESTADO_VENTA,
            ROW_NUMBER()OVER (PARTITION BY VARIEDAD.DES_VARIEDAD ORDER BY STOCK.FECHA_ESTIMADA_VENCIMIENTO DESC) AS N_REP_FRUTA
        FROM
            STOCK_SOBRANTE STOCK
                LEFT JOIN VENTA_LOCAL VENTA
                    ON STOCK.ID_STOCK = VENTA.ID_STOCK AND VENTA.ID_VENTA_LOCAL = (SELECT MAX(VENTA_2.ID_VENTA_LOCAL) FROM VENTA_LOCAL VENTA_2 WHERE VENTA_2.ID_STOCK = VENTA.ID_STOCK)
                INNER JOIN VARIEDAD VARIEDAD
                    ON STOCK.ID_VARIEDAD = VARIEDAD.ID_VARIEDAD
                INNER JOIN ESPECIE ESPECIE
                    ON VARIEDAD.ID_ESPECIE = ESPECIE.ID_ESPECIE
                LEFT JOIN IMAGEN IMAGEN
                    ON VARIEDAD.ID_IMAGEN = IMAGEN.ID_IMAGEN
        WHERE
            VENTA.ID_ESTADO = 1 OR VENTA.ID_ESTADO IS NULL
        ORDER BY
            VARIEDAD.DES_VARIEDAD;
    EXCEPTION --control de excepciones
        WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLERRM);
END SP_SALDOS;

-- /

-- CREATE OR REPLACE PROCEDURE SP_SOLICITUDES_ACEPTADAS AS
--     BEGIN
--         INSERT INTO ORDEN_COMPRA
--             (ID_ORDEN, DIFERENCIA_FRUTA,ID_VARIEDAD, ID_SOLICITUD, ID_ESTADO)
--         SELECT 
--             SQ_ID_ORDEN.NEXTVAL,
--             DETA_OFER.KILOS_TOTAL - DETA_SOLI.KILOS DIFF_KILOS,
--             DETA_SOLI.ID_VARIEDAD,
--             DETA_SOLI.ID_SOLICITUD,
--             1 AS ESTADO_PEDIDO
--         FROM DETALLE_SOLICITUD DETA_SOLI
--             INNER JOIN SOLICITUD SOLI
--                 ON DETA_SOLI.ID_SOLICITUD = SOLI.ID_SOLICITUD
--             INNER JOIN OFERTA_PRODUCTOR OFER_PROD
--                 ON SOLI.ID_SOLICITUD = OFER_PROD.ID_SOLICITUD
--             INNER JOIN DETALLE_OFERTA DETA_OFER 
--                 ON OFER_PROD.ID_OFERTA = DETA_OFER.ID_OFERTA AND DETA_SOLI.ID_VARIEDAD = DETA_OFER.ID_VARIEDAD
--         WHERE
--             SOLI.ID_ESTADO = 2;-- AND DETA_SOLI.ID_SOLICITUD NOT IN (SELECT ID_SOLICITUD FROM ORDEN_COMPRA);
-- END SP_SOLICITUDES_ACEPTADAS;

-- /

-- CREATE OR REPLACE PROCEDURE SP_ACTUALIZAR_STOCK AS
--     BEGIN
--         INSERT INTO STOCK_SOBRANTE
--             (ID_STOCK, ID_ORDEN, KILOS, ID_VARIEDAD, FECHA_COSECHA, FECHA_ESTIMADA_VENCIMIENTO, PRECIO_KILO)
--         SELECT
--             SQ_ID_STOCK.NEXTVAL,
--             ORDE_COMP.ID_ORDEN,
--             ORDE_COMP.DIFERENCIA_FRUTA,
--             ORDE_COMP.ID_VARIEDAD,
--             DETA_OFER.FECHA_COSECHA,
--             DETA_OFER.FECHA_COSECHA + VARI.DIAS_VENCIMIENTO,
--             ROUND((DETA_OFER.PRECIO_TOTAL/DETA_OFER.KILOS_TOTAL)*1.5)
--         FROM ORDEN_COMPRA ORDE_COMP
--             INNER JOIN SOLICITUD SOLI
--                 ON ORDE_COMP.ID_SOLICITUD = SOLI.ID_SOLICITUD
--             INNER JOIN DETALLE_SOLICITUD DETA_SOLI
--                 ON SOLI.ID_SOLICITUD = DETA_SOLI.ID_SOLICITUD AND ORDE_COMP.ID_VARIEDAD = DETA_SOLI.ID_VARIEDAD
--             INNER JOIN OFERTA_PRODUCTOR OFER_PROD
--                 ON SOLI.ID_SOLICITUD = OFER_PROD.ID_SOLICITUD
--             INNER JOIN DETALLE_OFERTA DETA_OFER 
--                 ON OFER_PROD.ID_OFERTA = DETA_OFER.ID_OFERTA AND DETA_SOLI.ID_VARIEDAD = DETA_OFER.ID_VARIEDAD
--             INNER JOIN VARIEDAD VARI
--                 ON ORDE_COMP.ID_VARIEDAD = VARI.ID_VARIEDAD
--         WHERE
--             ORDE_COMP.ID_ORDEN NOT IN (SELECT ID_ORDEN FROM STOCK_SOBRANTE);
-- END SP_ACTUALIZAR_STOCK;

/

CREATE OR REPLACE VIEW VIEW_LISTA_SOLICITUDES AS (
    SELECT
        SOLI.ID_SOLICITUD,
        SOLI.ID_USUARIO,
        SOLI.FECHA_CREACION,
        SOLI.PUB_HORA_INI,
        SOLI.PUB_HORA_FIN,
        ESPE.DES_ESPECIE,
        VARI.DES_VARIEDAD,
        DETA.KILOS,
        DETA.KILOS_OBTE,
        DETA.ID_PEDIDO,
        SOLI.ID_ESTADO,
        SOLI.ID_PUBLICACION
    FROM SOLICITUD SOLI
        INNER JOIN DETALLE_SOLICITUD DETA
            ON SOLI.ID_SOLICITUD = DETA.ID_SOLICITUD
        INNER JOIN VARIEDAD VARI
            ON DETA.ID_VARIEDAD = VARI.ID_VARIEDAD
        INNER JOIN ESPECIE ESPE
            ON VARI.ID_ESPECIE = ESPE.ID_ESPECIE
);

/

CREATE OR REPLACE VIEW VIEW_OFERTAS_PRODUCTOR AS (
    SELECT
        DETA_OFER.ID_DETALLE_OF,
        DETA_OFER.KILOS_TOTAL,
        DETA_OFER.PRECIO_TOTAL,
        DETA_OFER.FECHA_COSECHA,
        DETA_OFER.CERRADA,
        DETA_OFER.ID_USUARIO,
        OFER_PROD.ID_OFERTA,
        OFER_PROD.ID_SOLICITUD,
        DETA_SOLI.ID_PEDIDO,
        TRIM(CONCAT(CONCAT(USUA.NOMBRE, ' '), USUA.AP_PATERNO)) NOMBRE_USUARIO
    FROM DETALLE_OFERTA DETA_OFER
        INNER JOIN OFERTA_PRODUCTOR OFER_PROD
            ON DETA_OFER.ID_OFERTA = OFER_PROD.ID_OFERTA
        INNER JOIN USUARIO USUA
            ON DETA_OFER.ID_USUARIO = USUA.ID_USUARIO
        INNER JOIN DETALLE_SOLICITUD DETA_SOLI
            ON OFER_PROD.ID_SOLICITUD = DETA_SOLI.ID_SOLICITUD AND DETA_SOLI.ID_PEDIDO = DETA_OFER.ID_PEDIDO
);

/

CREATE OR REPLACE VIEW VIEW_DATOS_COTIZACION AS (
    SELECT 
        DETA_OFER.ID_DETALLE_OF,
        DETA_SOLI.ID_SOLICITUD,
        DETA_OFER.PRECIO_TOTAL,
        DETA_OFER.FECHA_COSECHA,
        DETA_OFER.CERRADA,
        ESPE.DES_ESPECIE,
        VARI.DES_VARIEDAD,
        USUA.ID_USUARIO,
        USUA.RUN_USUARIO,
        TRIM(CONCAT(CONCAT(USUA.NOMBRE, ' '), USUA.AP_PATERNO)) NOMBRE_USUARIO,
        CONCAT(CONCAT(USUA.DIRECCION, ', '), COMU.DES_COMUNA) DIRECCION,
        USUA.EMAIL CORREO,
        DETA_OFER.ID_PEDIDO,
        DETA_SOLI.KILOS,
        DETA_SOLI.KILOS_OBTE,
        ORDE.ID_ESTADO ID_ESTADO_ORDEN,
        SOLI.ID_PUBLICACION ID_ESTADO_PUBLICACION
    FROM DETALLE_OFERTA DETA_OFER
        INNER JOIN DETALLE_SOLICITUD DETA_SOLI
            ON DETA_OFER.ID_PEDIDO = DETA_SOLI.ID_PEDIDO
       INNER JOIN SOLICITUD SOLI
            ON DETA_SOLI.ID_SOLICITUD = SOLI.ID_SOLICITUD
        INNER JOIN VARIEDAD VARI
            ON DETA_OFER.ID_VARIEDAD = VARI.ID_VARIEDAD
        INNER JOIN ESPECIE ESPE
            ON VARI.ID_ESPECIE = ESPE.ID_ESPECIE
        INNER JOIN USUARIO USUA
            ON DETA_OFER.ID_USUARIO = USUA.ID_USUARIO
        INNER JOIN COMUNA COMU
            ON USUA.ID_COMUNA = COMU.ID_COMUNA
        LEFT JOIN ORDEN_COMPRA ORDE
            ON DETA_SOLI.ID_SOLICITUD = ORDE.ID_SOLICITUD
);

/

CREATE OR REPLACE VIEW VIEW_PEDIDOS_ACEPTADOS AS (
    SELECT
        ORDE_COMP.ID_ORDEN,
        ORDE_COMP.FECHA_RECEPCION,
        ORDE_COMP.ID_SOLICITUD,
        ORDE_COMP.ID_ESTADO ID_ESTADO_PEDIDO,
        ESTA_PEDI.DESC_ESTADO
    FROM
        ORDEN_COMPRA ORDE_COMP
            INNER JOIN ESTADO_PEDIDO ESTA_PEDI
                ON ORDE_COMP.ID_ESTADO = ESTA_PEDI.ID_ESTADO
);

/
     
CREATE OR REPLACE VIEW VIEW_CANTIDAD_SOLICITUDES_PENDIENTES AS (
    SELECT
        ESTA_SOLI.DES_ESTADO,
        COUNT(DISTINCT(SOLI.ID_SOLICITUD)) CANTIDAD_SOLICITUDES
    FROM
        SOLICITUD SOLI
            RIGHT OUTER JOIN ESTADO_SOLICITUD ESTA_SOLI
                ON SOLI.ID_ESTADO = ESTA_SOLI.ID_ESTADO
    WHERE
        SOLI.ID_ESTADO = 1
    GROUP BY
        ESTA_SOLI.DES_ESTADO
);

/

CREATE OR REPLACE VIEW VIEW_CANTIDAD_OC_RECHAZADAS AS (
    SELECT
        ESTA_PEDI.DESC_ESTADO,
        COUNT(DISTINCT(ORDEN.ID_ORDEN)) CANTIDAD_OC
    FROM
        ORDEN_COMPRA ORDEN
            RIGHT OUTER JOIN ESTADO_PEDIDO ESTA_PEDI
                ON ORDEN.ID_ESTADO = ESTA_PEDI.ID_ESTADO
    WHERE
        ORDEN.ID_ESTADO = 4
    GROUP BY
        ESTA_PEDI.DESC_ESTADO
);

/

CREATE OR REPLACE VIEW VIEW_CANTIDAD_PUBLICACIONES_X_ESTADO AS (
    SELECT 
        ESTA_PUBL.ID_ESTADO,
        ESTA_PUBL.DES_ESTADO,
        COUNT(DISTINCT(VIEW_LISTA.ID_SOLICITUD)) CANTIDAD_PUBLICACIONES
    FROM VIEW_LISTA_SOLICITUDES VIEW_LISTA
        RIGHT JOIN ESTADO_PUBLICACION ESTA_PUBL
            ON VIEW_LISTA.ID_PUBLICACION = ESTA_PUBL.ID_ESTADO
    WHERE
        VIEW_LISTA.ID_ESTADO = 2 OR VIEW_LISTA.ID_SOLICITUD IS NULL
    GROUP BY
        ESTA_PUBL.DES_ESTADO, ESTA_PUBL.ID_ESTADO
    --ORDER BY
        --ESTA_PUBL.ID_ESTADO
);
    
/

CREATE OR REPLACE VIEW VIEW_GANANCIAS_X_MES AS (
    SELECT
        MESES.ID_MES N_MES,
        SUM(MONTO) VENDIDO_MES
    FROM 
        PAGO PAG
            RIGHT JOIN 
                        (
                        SELECT
                            EXTRACT(MONTH FROM TO_DATE('2020-12-01', 'yyyy-mm-dd')) - (LEVEL - 1) ID_MES
                        FROM
                            DUAL
                        CONNECT BY
                            LEVEL <= 12
                        ) MESES
                ON TO_CHAR(PAG.FECHA_PAGO, 'MM') = MESES.ID_MES
    GROUP BY
        MESES.ID_MES        
);        

/

CREATE OR REPLACE VIEW VIEW_COSTOS_X_MES AS (
    SELECT
        MESES.ID_MES N_MES,
        SUM(COST.VALOR) COSTOS_MES
    FROM 
        COSTOS COST
        INNER JOIN STOCK_SOBRANTE STOCK
            ON COST.ID_ORDEN = STOCK.ID_ORDEN
        INNER JOIN VENTA_LOCAL VENT
            ON VENT.ID_STOCK = STOCK.ID_STOCK
        INNER JOIN PAGO PAG
            ON PAG.ID_VENTA_LOCAL = VENT.ID_VENTA_LOCAL
        RIGHT JOIN 
                        (
                        SELECT
                            EXTRACT(MONTH FROM TO_DATE('2020-12-01', 'yyyy-mm-dd')) - (LEVEL - 1) ID_MES
                        FROM
                            DUAL
                        CONNECT BY
                            LEVEL <= 12
                        ) MESES
                ON TO_CHAR(PAG.FECHA_PAGO, 'MM') = MESES.ID_MES
    GROUP BY
        MESES.ID_MES        
);

/

CREATE OR REPLACE VIEW VIEW_FRUTAS_DONADAS AS (
    SELECT      
        ESPECIE.DES_ESPECIE,
        VARIEDAD.DES_VARIEDAD,
        SUM(STOCK.KILOS) KILOS_DONADOS          
    FROM
        STOCK_SOBRANTE STOCK
            INNER JOIN VARIEDAD VARIEDAD
                ON STOCK.ID_VARIEDAD = VARIEDAD.ID_VARIEDAD
            INNER JOIN ESPECIE ESPECIE
                ON VARIEDAD.ID_ESPECIE = ESPECIE.ID_ESPECIE
    WHERE
    STOCK.FECHA_ESTIMADA_VENCIMIENTO < TO_DATE('03/12/2020','DD/MM/YYYY') AND STOCK.KILOS > 0
    GROUP BY
        ESPECIE.DES_ESPECIE, VARIEDAD.DES_VARIEDAD
);

/

CREATE OR REPLACE VIEW VIEW_PREFERENCIAS_BANCO AS (
    SELECT 
        BAN.DES_BANCO,
        COUNT(ID_PAGO) CANTIDAD_USADO
    FROM PAGO PAG
        INNER JOIN BANCO BAN
            ON PAG.ID_BANCO = BAN.ID_BANCO AND PAG.ID_BANCO <> -1
    GROUP BY
        BAN.DES_BANCO
);

/

CREATE OR REPLACE VIEW VIEW_PRODUCTORES_OFERTAS_APROBADAS AS (
    SELECT
        CONCAT(CONCAT(USUA.ID_USUARIO, ' - '), CONCAT(SUBSTR(USUA.NOMBRE, 0, INSTR(USUA.NOMBRE, ' ', 1)), USUA.AP_PATERNO)) NOMBRE_PRODUCTOR,
        COUNT(DETA_OFER.ID_PEDIDO) CANTIDAD_OFERTAS_APROBADAS
    FROM 
        DETALLE_OFERTA DETA_OFER
            INNER JOIN USUARIO USUA
                ON DETA_OFER.ID_USUARIO = USUA.ID_USUARIO
    WHERE
        DETA_OFER.CERRADA = 1
    GROUP BY
        USUA.ID_USUARIO,USUA.NOMBRE, USUA.AP_PATERNO
);

/

CREATE OR REPLACE VIEW VIEW_EXTERNO_ORDENES_RECHAZADAS AS (
    SELECT
        CONCAT(CONCAT(USUA.ID_USUARIO, ' - '), CONCAT(SUBSTR(USUA.NOMBRE, 0, INSTR(USUA.NOMBRE, ' ', 1)), USUA.AP_PATERNO)) NOMBRE_COMERCIANTE_EXT,
        COUNT(USUA.ID_USUARIO) CANTIDAD_ORDENES_RECHAZADAS
    FROM
        COSTOS COST
            INNER JOIN USUARIO USUA
                ON SUBSTR(SUBSTR(DESCRIPCION, INSTR(DESCRIPCION, ':') + 2, 1000), 0, INSTR(SUBSTR(DESCRIPCION, INSTR(DESCRIPCION, ':') + 2, 1000), ' ')) = USUA.ID_USUARIO
    WHERE
        SUBSTR(DESCRIPCION, 0, INSTR(DESCRIPCION, ' ') - 1) = 'Rechazada'
    GROUP BY
        USUA.ID_USUARIO,USUA.NOMBRE, USUA.AP_PATERNO
);

/

CREATE OR REPLACE VIEW VIEW_VENTA_LOCAL_EXTERNA AS (
    SELECT
        MESES.ID_MES N_MES,
        SUM(MONTO) VENDIDO_MES_LOCAL,
        VENDIDO_MES_EXTERNO
    FROM 
        PAGO PAG
            RIGHT JOIN (
                        SELECT
                            EXTRACT(MONTH FROM TO_DATE('2020-12-01', 'yyyy-mm-dd')) - (LEVEL - 1) ID_MES
                        FROM
                            DUAL
                        CONNECT BY
                            LEVEL <= 12
                        ) MESES
                ON TO_CHAR(PAG.FECHA_PAGO, 'MM') = MESES.ID_MES
            INNER JOIN (
                        SELECT
                            MESES.ID_MES N_MES,
                            SUM(MONTO) VENDIDO_MES_EXTERNO
                        FROM 
                            PAGO PAG
                                RIGHT JOIN (
                                            SELECT
                                                EXTRACT(MONTH FROM TO_DATE('2020-12-01', 'yyyy-mm-dd')) - (LEVEL - 1) ID_MES
                                            FROM
                                                DUAL
                                            CONNECT BY
                                                LEVEL <= 12
                                            ) MESES
                                    ON TO_CHAR(PAG.FECHA_PAGO, 'MM') = MESES.ID_MES
                        WHERE
                            PAG.ID_BANCO = -1 OR MONTO IS NULL
                        GROUP BY
                            MESES.ID_MES 
                        ) GANANCIAS_EXTERNO
            ON MESES.ID_MES = GANANCIAS_EXTERNO.N_MES
    WHERE
        PAG.ID_BANCO <> -1 OR MONTO IS NULL
    GROUP BY
        MESES.ID_MES, VENDIDO_MES_EXTERNO
);

/

CREATE OR REPLACE VIEW VIEW_HISTORIAL_COMERCIANTE AS (
    SELECT
        PAG.ID_VENTA_LOCAL N_VENTA,
        PAG.FECHA_PAGO FECHA_COMPRA,
        CONCAT(ESPE.DES_ESPECIE, CONCAT(' ', VARI.DES_VARIEDAD)) FRUTA,
        VENT_LOCA.KILOS_COMPRADOS,
        PAG.MONTO,
        VENT_LOCA.ID_USUARIO
    FROM
        PAGO PAG
            INNER JOIN VENTA_LOCAL VENT_LOCA
                ON PAG.ID_VENTA_LOCAL = VENT_LOCA.ID_VENTA_LOCAL
            INNER JOIN STOCK_SOBRANTE STOC_SOBRA
                ON VENT_LOCA.ID_STOCK = STOC_SOBRA.ID_STOCK
            INNER JOIN VARIEDAD VARI
                ON STOC_SOBRA.ID_VARIEDAD = VARI.ID_VARIEDAD
            INNER JOIN ESPECIE ESPE
                ON VARI.ID_ESPECIE = ESPE.ID_ESPECIE
);

/

CREATE OR REPLACE VIEW VIEW_HISTORIAL_EXTERNO AS (
    SELECT
        ORDE_COMP.ID_SOLICITUD N_VENTA,
        ORDE_COMP.FECHA_RECEPCION,
        CONCAT(ESPE.DES_ESPECIE, CONCAT(' ', VARI.DES_VARIEDAD)) FRUTA,
        DETA_SOLI.KILOS KILOS_SOLICITADOS,
        COST.VALOR MONTO,
        TRIM(SUBSTR(COST.DESCRIPCION, 0, INSTR(COST.DESCRIPCION, ' '))) ESTADO,
        ROW_NUMBER()OVER (PARTITION BY ORDE_COMP.ID_SOLICITUD ORDER BY ORDE_COMP.ID_SOLICITUD) AS N_REP_SOLICITUD,
        SUBSTR(SUBSTR(COST.DESCRIPCION, INSTR(COST.DESCRIPCION, ':') + 2, 1000), 0, INSTR(SUBSTR(COST.DESCRIPCION, INSTR(COST.DESCRIPCION, ':') + 2, 1000), ' ')) ID_USUARIO
    FROM
        COSTOS COST
            INNER JOIN ORDEN_COMPRA ORDE_COMP
                ON COST.ID_ORDEN = ORDE_COMP.ID_ORDEN
            INNER JOIN DETALLE_SOLICITUD DETA_SOLI
                ON ORDE_COMP.ID_SOLICITUD = DETA_SOLI.ID_SOLICITUD
            INNER JOIN VARIEDAD VARI
                ON DETA_SOLI.ID_VARIEDAD = VARI.ID_VARIEDAD
            INNER JOIN ESPECIE ESPE
                ON VARI.ID_ESPECIE = ESPE.ID_ESPECIE
);

/

CREATE OR REPLACE VIEW VIEW_HISTORIAL_PRODUCTOR AS (
    SELECT
        DETA_OFER.ID_DETALLE_OF N_OFERTA,
        DETA_OFER.ID_PEDIDO,
        DETA_OFER.FECHA_OFERTA,
        CONCAT(ESPE.DES_ESPECIE, CONCAT(' ', VARI.DES_VARIEDAD)) FRUTA,
        DETA_OFER.KILOS_TOTAL KILOS_VENDIDOS,
        DETA_OFER.PRECIO_TOTAL,
        DETA_OFER.CERRADA,
        ROW_NUMBER()OVER (PARTITION BY DETA_OFER.ID_PEDIDO ORDER BY DETA_OFER.CERRADA DESC) AS N_REP_OFERTA,
        DETA_OFER.ID_USUARIO
    FROM DETALLE_OFERTA DETA_OFER
        INNER JOIN VARIEDAD VARI
            ON DETA_OFER.ID_VARIEDAD = VARI.ID_VARIEDAD
        INNER JOIN ESPECIE ESPE
            ON VARI.ID_ESPECIE = ESPE.ID_ESPECIE
);


COMMIT;
