from django.contrib import admin
#from .models import Cliente
from .models import CATEGORIA
from .models import Proveedor
from .models import Producto
from .models import Marca
from .models import Bodega
from .models import Empleado
from .models import Cliente
from .models import Modelo
#from .models import BodegaProductos

# Register your models here.
admin.site.register(CATEGORIA)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Empleado)
admin.site.register(Bodega)
admin.site.register(Cliente)
admin.site.register(Modelo)
#admin.site.register(BodegaProductos)





