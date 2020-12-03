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
