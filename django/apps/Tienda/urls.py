from django.urls import path
from . import views
from django.contrib import messages



urlpatterns = [
    path('', views.cargarInicio),
    path('agregarProducto', views.cargarAgregarProducto),
    path('agregarProd',views.agregarProducto),
    path('editarProducto/<id>',views.cargarEditarProducto),
    path('editarProductoForm',views.editarProducto),
    path('eliminarProducto/<id>',views.eliminarProducto),
    path('contactanos',views.cargarContactanos),
    path('registro',views.registro),
    path('api/', views.api),
    
]