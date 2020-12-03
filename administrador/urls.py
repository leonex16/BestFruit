from django.urls import path
from .views import home, ordenCompra, solicitud, publicacion, estadisticas

urlpatterns = [
   path('', home, name="home"),
   path('solicitud/', solicitud, name="solicitud"),
   path('publicacion/', publicacion, name="publicacion"),
   path('ordenCompra/', ordenCompra, name="ordenCompra"),
   path('estadisticas/', estadisticas, name="estadisticas")
] 
