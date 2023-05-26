from django.contrib import admin
from django.urls import path
# Importamos las clases creadas en el archivo views
#from .views import EmpleadoView
from .views import ProveedorView
from .views import CategoriaView
from .views import ProductoView
from .views import MarcaView
from .views import BodegaView
from .views import EmpleadoView
from .views import CategoriaView
from .views import ClienteView
from .views import ModeloView

#from . import views

urlpatterns = [    
    path('proveedors/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedors/<int:id>', ProveedorView.as_view(), name='proveedor_process'),
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/<int:id>', CategoriaView.as_view(), name='categoria_process'),   
    path('productos/', ProductoView.as_view(), name='producto_list'),
    path('productos/<int:id>', ProductoView.as_view(), name='producto_process'),
    path('marcas/', MarcaView.as_view(), name='marcas_list'),
    path('marcas/<int:id>', MarcaView.as_view(), name='marcas_process'),
    path('empleados/', EmpleadoView.as_view(), name='empleado_list'),
    path('empleados/<int:id>', EmpleadoView.as_view(), name='empleado_process'),
    path('bodegas/', BodegaView.as_view(), name='sucursal_list'),  
    path('bodegas/<int:id>', BodegaView.as_view(), name='sucursal_process'),
    path('clientes/', ClienteView.as_view(), name='cliente_list'),
    path('clientes/<int:id>', ClienteView.as_view(), name='cliente_process'), 
    path('modelos/', ModeloView.as_view(), name='modelo_list'),
    path('modelos/<int:id>', ModeloView.as_view(), name='modelo_process')

]

