from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("auto_create/", views.auto_create, name = "AutoNuevo"),
    path("sucursal_create/", views.sucursal_create, name = "SucursalNueva"),
    path("venta_create/", views.venta_create, name = "VentaNueva"),
    path('buscar_auto/', views.buscar_auto, name="BuscarAuto"),
    path("listar_autos/", views.lista_autos, name = "ListarAutos"),
    path("listar_ventas/", views.lista_ventas, name = "ListarVentas"),
    path("listar_sucursales/", views.lista_sucursal, name = "ListarSucursales"),
]