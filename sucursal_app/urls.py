from django.urls import path
from sucursal_app import views

urlpatterns = [
    path("sucursal", views.inicio_vistaSucursales, name="sucursal"),
    path("registrarSucursal/",views.registrarSucursal,name="registrarSucursal"),
    path("seleccionarSucursal/<id_sucursal>",views.seleccionarSucursal,name="seleccionarSucursal"),
    path("editarSucursal/",views.editarSucursal,name="editarSucursal"),
    path("borrarSucursal/<id_sucursal>",views.borrarSucursal,name="borrarSucursal")
]