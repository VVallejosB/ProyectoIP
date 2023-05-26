from django.http.response import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import CATEGORIA
from .models import Proveedor
from .models import Producto
from .models import Marca
from .models import Empleado
from .models import Bodega
from .models import Cliente
from .models import Modelo
import json
# Create your views here.

class EmpleadoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            empleados=list(Empleado.objects.filter(ID_EMPLEADO=id).values())
            if len(empleados) > 0:
                empleado=empleados[0]
                datos = {'message':"Success",'empleado': empleado}
            else:
                datos = {'message': "Empleado not found..."}
            return JsonResponse(datos)
        else:
            empleados = list(Empleado.objects.values())
            if len(empleados) > 0:
                datos = {'message':"Success",'empleados': empleados}
            else:
                datos = {'message': "empleados not found..."}
            return JsonResponse(datos)
        
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Empleado.objects.create(ID_EMPLEADO=jd['ID_EMPLEADO'], RUT_EMPLEADO=jd['RUT_EMPLEADO'],  NOMBRE_EMPLEADO=jd['NOMBRE_EMPLEADO'], APELLIDO_EMPLEADO=jd['APELLIDO_EMPLEADO'], TELEFONO_EMPLEADO=jd['TELEFONO_EMPLEADO'], DIRECCION=jd['DIRECCION'])
        datos={'message': "Success"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        empleaados=list(Empleado.objects.filter(ID_EMPLEADO=id).values())
        if len(empleaados) > 0:
            empleado=Empleado.objects.get(ID_EMPLEADO=id)
            empleado.ID_EMPLEADO=jd['ID_EMPLEADO']
            empleado.RUT_EMPLEADO=jd['RUT_EMPLEADO']
            empleado.NOMBRE_EMPLEADO=jd['NOMBRE_EMPLEADO']
            empleado.APELLIDO_EMPLEADO=jd['APELLIDO_EMPLEADO']
            empleado.TELEFONO_EMPLEADO=jd['TELEFONO_EMPLEADO']
            empleado.DIRECCION=jd['DIRECCION']
            empleado.save()
            datos={'message': "Success"}
        else: 
            datos = {'message': "Empleado not found..."}
        return JsonResponse(datos)

    def delete(self,request,id):
        empleados = list(Empleado.objects.filter(ID_EMPLEADO=id).values())  
        if len(empleados) > 0:
            Empleado.objects.filter(ID_EMPLEADO=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Empleado not found..."}
        return JsonResponse(datos)
    



class BodegaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            bodegas = list(Bodega.objects.filter(ID_BODEGA=id).values())
            if len(bodegas) > 0:
                bodega = bodegas[0]
                datos = {'message': "Success", 'bodega': bodega}
            else:
                datos = {'message': "bodega not found..."}
            return JsonResponse(datos)
        else:
            bodegas = list(Bodega.objects.values())
            if len(bodegas) > 0:
                datos = {'message': "Success", 'bodegas': bodegas}
            else:
                datos = {'message': "bodegas not found..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Bodega.objects.create(ID_BODEGA=jd['ID_BODEGA'], DIRECCION=jd['DIRECCION'], STOCK=jd['STOCK'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        bodegas = list(Bodega.objects.filter(ID_BODEGA=id).values())
        if len(bodegas) > 0:
            bodega = Bodega.objects.get(ID_BODEGA=id)
            bodega.ID_BODEGA = jd['ID_BODEGA']
            bodega.DIRECCION = jd['DIRECCION']
            bodega.STOCK = jd['STOCK']
            bodega.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Bodega not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        bodegas = list(Bodega.objects.filter(ID_BODEGA=id).values())
        if len(bodegas) > 0:
            Bodega.objects.filter(ID_BODEGA=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Bodega not found..."}
        return JsonResponse(datos)

    def add_product_to_bodega(self, request, bodega_id):
        jd = json.loads(request.body)
        bodega = Bodega.objects.get(ID_BODEGA=bodega_id)
        producto_id = jd['producto_id']
        cantidad = jd['cantidad']

        try:
            producto = Producto.objects.get(ID_PRODUCTO=producto_id)
        except Producto.DoesNotExist:
            datos = {'message': "Product not found..."}
            return JsonResponse(datos)

        bodega.productos.add(producto, through_defaults={'cantidad': cantidad})

        datos = {'message': "Success"}
        return JsonResponse(datos)


        

class ProductoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            productos=list(Producto.objects.filter(ID_PRODUCTO=id).values())
            if len(productos) > 0:
                producto=productos[0]
                datos = {'message':"Success",'productos': producto}
            else:
                datos = {'message': "productos not found..."}
            return JsonResponse(datos)
        else:
            productos = list(Producto.objects.values())
            if len(productos) > 0:
                datos = {'message':"Success",'productos': productos}
            else:
                datos = {'message': "productos not found..."}
            return JsonResponse(datos)
        
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Producto.objects.create(ID_PRODUCTO=jd['ID_PRODUCTO'], nombreProducto=jd['nombreProducto'])
        datos={'message': "Success"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        productos=list(Producto.objects.filter(ID_PRODUCTO=id).values())
        if len(productos) > 0:
            producto=Producto.objects.get(ID_PRODUCTO=id)
            producto.ID_PRODUCTO=jd['ID_PRODUCTO']
            producto.nombreProducto=jd['nombreProducto']
            producto.save()
            datos = {'message': "succes"}
        else: 
            datos = {'message': "productos not found..."}
        return JsonResponse(datos)

    def delete(self,request,id):
        productos = list(Producto.objects.filter(ID_PRODUCTO=id).values())  
        if len(productos) > 0:
            Producto.objects.filter(ID_PRODUCTO=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "productos not found..."}
        return JsonResponse(datos)

        




class MarcaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            marcas=list(Marca.objects.filter(ID_MARCA=id).values())
            if len(marcas) > 0:
                marca=marcas[0]
                datos = {'message':"Success",'marcas': marca}
            else:
                datos = {'message': "marcas not found..."}
            return JsonResponse(datos)
        else:
            marcas = list(Marca.objects.values())
            if len(marcas) > 0:
                datos = {'message':"Success",'marcas': marcas}
            else:
                datos = {'message': "marcas not found..."}
            return JsonResponse(datos)
        
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Marca.objects.create(ID_MARCA=jd['ID_MARCA'], nombreMarca=jd['nombreMarca'])
        datos={'message': "Success"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        marcas=list(Marca.objects.filter(ID_MARCA=id).values())
        if len(marcas) > 0:
            marca=Marca.objects.get(ID_MARCA=id)
            marca.ID_MARCA=jd['ID_MARCA']
            marca.nombreMarca=jd['nombreMarca']
            marca.save()
            datos = {'message': "succes"}
        else: 
            datos = {'message': "marcas not found..."}
        return JsonResponse(datos)

    def delete(self,request,id):
        marcas = list(Marca.objects.filter(ID_MARCA=id).values())  
        if len(marcas) > 0:
            Marca.objects.filter(ID_MARCA=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "marcas not found..."}
        return JsonResponse(datos)

        

class ProveedorView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            proveedores=list(Proveedor.objects.filter(ID_PROVEEDOR=id).values())
            if len(proveedores) > 0:
                proveedor=proveedores[0]
                datos = {'message':"Success",'proveedor': proveedor}
            else:
                datos = {'message': "Proveedor not found..."}
            return JsonResponse(datos)
        else:
            proveedores = list(Proveedor.objects.values())
            if len(proveedores) > 0:
                datos = {'message':"Success",'proveedores': proveedores}   
            else:
                datos = {'message': "Proveedores not found..."}
            return JsonResponse(datos)
        
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Proveedor.objects.create(ID_PROVEEDOR=jd['ID_PROVEEDOR'], 
                                 RUT_PROVEEDOR=jd['RUT_PROVEEDOR'],  
                                 NOMBRE_PROVEEDOR=jd['NOMBRE_PROVEEDOR'],
                                 TELEFONO_PROVEEDOR=jd['TELEFONO_PROVEEDOR'], 
                                 DIRECCION=jd['DIRECCION'])
        datos={'message': "Success"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        proveedores=list(Proveedor.objects.filter(ID_PROVEEDOR=id).values())
        if len(proveedores) > 0:
            proveedor=Proveedor.objects.get(ID_PROVEEDOR=id)
            proveedor.ID_PROVEEDOR=jd['ID_PROVEEDOR']
            proveedor.RUT_PROVEEDOR=jd['RUT_PROVEEDOR']
            proveedor.NOMBRE_PROVEEDOR=jd['NOMBRE_PROVEEDOR']
            proveedor.TELEFONO_PROVEEDOR=jd['TELEFONO_PROVEEDOR']
            proveedor.DIRECCION=jd['DIRECCION']
            proveedor.save()
            datos={'message': "Success"}
        else: 
            datos = {'message': "Proveedor not found..."}
        return JsonResponse(datos)

    def delete(self,request,id):
        proveedores = list(Proveedor.objects.filter(ID_PROVEEDOR=id).values())  
        if len(proveedores) > 0:
            Proveedor.objects.filter(ID_PROVEEDOR=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Proveedor not found..."}
        return JsonResponse(datos)
    

class CategoriaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            categorias=list(CATEGORIA.objects.filter(ID_CATEGORIA=id).values())
            if len(categorias) > 0:
                categoria=categorias[0]
                datos = {'message':"Success",'categorias': categoria}
            else:
                datos = {'message': "categorias not found..."}
            return JsonResponse(datos)
        else:
            categorias = list(CATEGORIA.objects.values())
            if len(categorias) > 0:
                datos = {'message':"Success",'categorias': categorias}
            else:
                datos = {'message': "categorias not found..."}
            return JsonResponse(datos)
        
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        CATEGORIA.objects.create(ID_CATEGORIA=jd['ID_CATEGORIA'], nombreCategoria=jd['nombreCategoria'])
        datos={'message': "Success"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        categorias=list(CATEGORIA.objects.filter(ID_CATEGORIA=id).values())
        if len(categorias) > 0:
            categoria=CATEGORIA.objects.get(ID_CATEGORIA=id)
            categoria.ID_CATEGORIA=jd['ID_CATEGORIA']
            categoria.nombreCategoria=jd['nombreCategoria']
            categoria.save()
            datos = {'message': "succes"}
        else: 
            datos = {'message': "categorias not found..."}
        return JsonResponse(datos)

    def delete(self,request,id):
        categorias = list(CATEGORIA.objects.filter(ID_CATEGORIA=id).values())  
        if len(categorias) > 0:
            CATEGORIA.objects.filter(ID_CATEGORIA=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "categorias not found..."}
        return JsonResponse(datos)



class ClienteView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            clientes=list(Cliente.objects.filter(ID_CLIENTE=id).values())
            if len(clientes) > 0:
                cliente=clientes[0]
                datos = {'message':"Success",'cliente': cliente}
            else:
                datos = {'message': "Cliente not found..."}
            return JsonResponse(datos)
        else:
            clientes = list(Cliente.objects.values())
            if len(clientes) > 0:
                datos = {'message':"Success",'clientes': clientes}
            else:
                datos = {'message': "clientes not found..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Cliente.objects.create(ID_CLIENTE=jd['ID_CLIENTE'], 
                                 RUT_CLIENTE=jd['RUT_CLIENTE'],  
                                 NOMBRE_CLIENTE=jd['NOMBRE_CLIENTE'], 
                                 APELLIDO_CLIENTE=jd['APELLIDO_CLIENTE'], 
                                 TELEFONO_CLIENTE=jd['TELEFONO_CLIENTE'], 
                                 DIRECCION_CLIENTE=jd['DIRECCION_CLIENTE'])
        datos={'message': "Success"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        clientes=list(Cliente.objects.filter(ID_CLIENTE=id).values())
        if len(clientes) > 0:
            cliente=Cliente.objects.get(ID_CLIENTE=id)
            cliente.ID_CLIENTE=jd['ID_CLIENTE']
            cliente.RUT_CLIENTE=jd['RUT_CLIENTE']
            cliente.NOMBRE_CLIENTE=jd['NOMBRE_CLIENTE']
            cliente.APELLIDO_CLIENTE=jd['APELLIDO_CLIENTE']
            cliente.TELEFONO_CLIENTE=jd['TELEFONO_CLIENTE']
            cliente.DIRECCION_CLIENTE=jd['DIRECCION_CLIENTE']
            cliente.save()
            datos={'message': "Success"}
        else: 
            datos = {'message': "Cliente not found..."}
        return JsonResponse(datos)

    def delete(self,request,id):
        clientes = list(Cliente.objects.filter(ID_CLIENTE=id).values())  
        if len(clientes) > 0:
            Cliente.objects.filter(ID_CLIENTE=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Cliente not found..."}
        return JsonResponse(datos)


class ModeloView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            modelos=list(Modelo.objects.filter(ID_MODELO=id).values())
            if len(modelos) > 0:
                modelo=modelos[0]
                datos = {'message':"Success",'modelos': modelo}
            else:
                datos = {'message': "modelos not found..."}
            return JsonResponse(datos)
        else:
            modelos = list(Modelo.objects.values())
            if len(modelos) > 0:
                datos = {'message':"Success",'modelos': modelos}
            else:
                datos = {'message': "modelos not found..."}
            return JsonResponse(datos)
        
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Modelo.objects.create(ID_MODELO=jd['ID_MODELO'],
                              NOMBRE_MODELO=jd['NOMBRE_MODELO'])
        datos={'message': "Success"}
        return JsonResponse(datos)

    def put(self,request, id):
        jd = json.loads(request.body)
        modelos=list(Modelo.objects.filter(ID_MODELO=id).values())
        if len(modelos) > 0:
            modelo=Modelo.objects.get(ID_MODELO=id)
            modelo.ID_MODELO=jd['ID_MODELO']
            modelo.NOMBRE_MODELO=jd['NOMBRE_MODELO']
            modelo.save()
            datos = {'message': "succes"}
        else: 
            datos = {'message': "modelos not found..."}
        return JsonResponse(datos)

    def delete(self,request,id):
        modelos = list(Modelo.objects.filter(ID_MODELO=id).values())  
        if len(modelos) > 0:
            Modelo.objects.filter(ID_MODELO=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "modelos not found..."}
        return JsonResponse(datos)


