from django.urls import path
from venta_app import views

urlpatterns = [
    path("venta", views.inicio_vistaVentas, name="venta"),
    path("registrarVenta/",views.registrarVenta,name="registrarVenta"),
    path("seleccionarVenta/<id_venta>",views.seleccionarVenta,name="seleccionarVenta"),
    path("editarVenta/",views.editarVenta,name="editarVenta"),
    path("borrarVenta/<id_venta>",views.borrarVenta,name="borrarVenta")
]