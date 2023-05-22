from django.urls import path
from . import views

urlpatterns=[

    path('producto/listado/', views.listado_productos, name='listado_productos'),
    path('proveedor/listado/', views.listado_proveedores, name='listado_proveedores'),
    path('productos/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('productos/modificar/<int:producto_id>', views.modificar_producto, name='modificar_producto'),
    path('proveedor/nuevo/', views.nuevo_proveedor, name='nuevo_proveedor'),
    path('proveedor/modificar/<int:proveedor_id>', views.modificar_proveedor, name='modificar_proveedor'),

]