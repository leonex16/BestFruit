from django.contrib import admin
from .models import Calidad, Calificacion, Comuna, Contrato, Costos, DetalleOferta, DetalleSolicitud, Especie, EstadoContrato, EstadoEmpresa, EstadoPedido, EstadoSolicitud, EstadoUsuario, EstadoVenta, Imagen, OfertaProductor, OrdenCompra, Pago, Pais, Provincia, Puntos, Region, Rol, Solicitud, StockSobrante, Usuario, Variedad, VentaLocal

admin.site.register(Calidad)
admin.site.register(Calificacion)
admin.site.register(Comuna)
admin.site.register(Contrato)
admin.site.register(Costos)
admin.site.register(DetalleOferta)
admin.site.register(DetalleSolicitud)
admin.site.register(Especie)
admin.site.register(EstadoContrato)
admin.site.register(EstadoEmpresa)
admin.site.register(EstadoPedido)
admin.site.register(EstadoSolicitud)
admin.site.register(EstadoUsuario)
admin.site.register(EstadoVenta)
admin.site.register(Imagen)
admin.site.register(OfertaProductor)
admin.site.register(OrdenCompra)
admin.site.register(Pago)
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Puntos)
admin.site.register(Region)
admin.site.register(Rol)
admin.site.register(Solicitud)
admin.site.register(StockSobrante)
admin.site.register(Usuario)
admin.site.register(Variedad)
admin.site.register(VentaLocal)

# Register your models here.
# clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)

# for nombreClase in clsmembers:
#     admin.site.register(nombreClase[1])
