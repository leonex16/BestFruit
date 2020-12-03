from django.urls import path
from .views import historial, home, informacionBestFruit, login, registro, detalle, solicitud, docPdf, pedido, informacion, publicacion, ofertarProducto, transbank

urlpatterns = [
   path('', home, name="home"),
   path('informacionBestFruit/', informacionBestFruit, name="informacionBestFruit"),
   path('login/', login, name="login"),
   path('registro/', registro, name="registro"),
   path('detalle/<int:id>', detalle, name="detalle"),
   path('transbank/<int:id>', transbank, name="transbank"),
   path('usuario/solicitud/', solicitud, name="solicitud"),
   path('pdf/', docPdf, name="pdf"),
   path('usuario/pedido/', pedido, name="pedido"),
   path('usuario/historial/', historial, name="historial"),
   path('usuario/informacion/', informacion, name="informacion"),
   path('usuario/publicacion/', publicacion, name="publicacion"),
   path('usuario/publicacion/<int:idSolicitud>/<int:idPedido>/<slug:fruta>', ofertarProducto, name="ofertarProducto"),
] 
