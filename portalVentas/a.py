# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Calidad(models.Model):
    id_calidad = models.BooleanField(primary_key=True)
    detalle = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'calidad'


class Calificacion(models.Model):
    id_calificacion = models.BooleanField(primary_key=True)
    des_calificacion = models.CharField(max_length=50)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calificacion'


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    des_comuna = models.CharField(max_length=50)
    id_provincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='id_provincia')

    class Meta:
        managed = False
        db_table = 'comuna'


class Contrato(models.Model):
    id_contrato = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    vigencia = models.CharField(max_length=1)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_estado = models.ForeignKey('EstadoContrato', models.DO_NOTHING, db_column='id_estado')

    class Meta:
        managed = False
        db_table = 'contrato'


class Costos(models.Model):
    id_costo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)
    valor = models.IntegerField(blank=True, null=True)
    id_orden = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='id_orden', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'costos'


class DetalleOferta(models.Model):
    id_detalle_of = models.IntegerField(primary_key=True)
    kilos_total = models.IntegerField()
    precio_total = models.IntegerField()
    fecha_cosecha = models.DateField()
    id_oferta = models.ForeignKey('OfertaProductor', models.DO_NOTHING, db_column='id_oferta')
    id_variedad = models.ForeignKey('Variedad', models.DO_NOTHING, db_column='id_variedad')
    id_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='id_solicitud')

    class Meta:
        managed = False
        db_table = 'detalle_oferta'


class DetalleSolicitud(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    id_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='id_solicitud')
    id_variedad = models.ForeignKey('Variedad', models.DO_NOTHING, db_column='id_variedad')
    kilos = models.DecimalField(max_digits=14, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'detalle_solicitud'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Especie(models.Model):
    id_especie = models.IntegerField(primary_key=True)
    des_especie = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'especie'


class EstadoContrato(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    des_estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_contrato'


class EstadoPedido(models.Model):
    id_estado = models.BooleanField(primary_key=True)
    desc_estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class EstadoPublicacion(models.Model):
    id_estado = models.BooleanField(primary_key=True)
    des_estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_publicacion'


class EstadoSolicitud(models.Model):
    id_estado = models.BooleanField(primary_key=True)
    des_estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_solicitud'


class EstadoUsuario(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    des_estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_usuario'


class EstadoVenta(models.Model):
    id_estado = models.BooleanField(primary_key=True)
    des_estado = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_venta'


class Imagen(models.Model):
    id_imagen = models.IntegerField(primary_key=True)
    desc_imagen = models.CharField(max_length=100)
    ext_imagen = models.CharField(max_length=6)
    imagen = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imagen'


class OfertaProductor(models.Model):
    id_oferta = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'oferta_productor'


class OrdenCompra(models.Model):
    id_orden = models.IntegerField(primary_key=True)
    diferencia_fruta = models.IntegerField()
    id_variedad = models.ForeignKey('Variedad', models.DO_NOTHING, db_column='id_variedad')
    id_solicitud = models.ForeignKey('Solicitud', models.DO_NOTHING, db_column='id_solicitud')
    id_estado = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_compra'


class Pago(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    id_banco = models.IntegerField()
    monto = models.IntegerField(blank=True, null=True)
    fecha_pago = models.DateField(blank=True, null=True)
    id_venta_local = models.ForeignKey('VentaLocal', models.DO_NOTHING, db_column='id_venta_local')

    class Meta:
        managed = False
        db_table = 'pago'


class Pais(models.Model):
    id_pais = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class Provincia(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    des_provincia = models.CharField(max_length=50)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'provincia'


class Puntos(models.Model):
    id_puntos = models.BooleanField(primary_key=True)
    des_puntos = models.CharField(max_length=50)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'puntos'


class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    des_region = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'


class Rol(models.Model):
    id_rol = models.BooleanField(primary_key=True)
    des_rol = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol'


class Solicitud(models.Model):
    id_solicitud = models.IntegerField(primary_key=True)
    fecha_creacion = models.DateField()
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_estado = models.ForeignKey(EstadoSolicitud, models.DO_NOTHING, db_column='id_estado', blank=True, null=True)
    hora_ini = models.DateTimeField(blank=True, null=True)
    hora_fin = models.DateTimeField(blank=True, null=True)
    id_publicacion = models.ForeignKey(EstadoPublicacion, models.DO_NOTHING, db_column='id_publicacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud'


class StockSobrante(models.Model):
    id_stock = models.IntegerField(primary_key=True)
    kilos = models.IntegerField(blank=True, null=True)
    fecha_cosecha = models.DateField(blank=True, null=True)
    fecha_estimada_vencimiento = models.DateField(blank=True, null=True)
    precio_kilo = models.IntegerField(blank=True, null=True)
    id_orden = models.ForeignKey(OrdenCompra, models.DO_NOTHING, db_column='id_orden', blank=True, null=True)
    id_variedad = models.ForeignKey('Variedad', models.DO_NOTHING, db_column='id_variedad')

    class Meta:
        managed = False
        db_table = 'stock_sobrante'


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    run_usuario = models.CharField(unique=True, max_length=30)
    nombre = models.CharField(max_length=50)
    ap_paterno = models.CharField(max_length=25)
    ap_materno = models.CharField(max_length=25)
    fecha_nac = models.DateField()
    email = models.CharField(unique=True, max_length=250)
    direccion = models.CharField(max_length=150)
    num_celular = models.IntegerField()
    clave = models.CharField(max_length=255)
    id_estado = models.ForeignKey(EstadoUsuario, models.DO_NOTHING, db_column='id_estado')
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna', blank=True, null=True)
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol')
    id_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='id_pais', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Variedad(models.Model):
    id_variedad = models.IntegerField(primary_key=True)
    des_variedad = models.CharField(max_length=50)
    dias_vencimiento = models.IntegerField()
    id_especie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='id_especie')
    id_imagen = models.ForeignKey(Imagen, models.DO_NOTHING, db_column='id_imagen', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variedad'


class VentaLocal(models.Model):
    id_venta_local = models.IntegerField(primary_key=True)
    kilos_iniciales = models.IntegerField()
    kilos_comprados = models.IntegerField()
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario')
    id_stock = models.ForeignKey(StockSobrante, models.DO_NOTHING, db_column='id_stock')
    id_estado = models.ForeignKey(EstadoVenta, models.DO_NOTHING, db_column='id_estado')

    class Meta:
        managed = False
        db_table = 'venta_local'
