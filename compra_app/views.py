from django.shortcuts import render
from compra_app.models import Proveedor, Producto
from django.views.generic import (CreateView)

# Create your views here.
def listado_proveedores(request):
    proveedores=Proveedor.objects.all()
    context={
        "proveedores":proveedores,

    }
    return render(request, "listado_proveedores.html", context)



def listado_productos(request):
    productos=Producto.objects.all()
    context={
        "productos":productos,

    }
    return render(request, "listado_productos.html", context)


def nuevo_proveedor(request): #nuevo
    
   
    if request.POST:
        nombre=request.POST['nombre']
        apellido=request.POST['apellido']
        dni=request.POST['dni']
       
        
        Proveedor.objects.create(
            nombre=nombre,
            apellido=apellido,
            dni=dni,
                    

        )

    return render(request,"nuevo_proveedor.html")


def nuevo_producto(request): #nuevo
    
    proveedores=Proveedor.objects.all()
    context={
        "proveedores":proveedores,

    }
    if request.POST:
        nombre=request.POST['nombre']
        precio=request.POST['precio']
        stock_actual=request.POST['stock_actual']
        proveedor_id=request.POST['proveedor']
        
        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            stock_actual=stock_actual,
            proveedor_id=proveedor_id,
            

        )

    return render(request,"nuevo_producto.html",context)

#class ProductoCreateView(CreateView): tarea

    
def modificar_producto(request, producto_id):

    
    proveedores=Proveedor.objects.all()
    producto=Producto.objects.get(id=producto_id) #recibo el producto por el id de la pagina

    context={
        "proveedores":proveedores,
        "producto":producto

    }


    if request.POST:
        nombre=request.POST['nombre']
        precio=request.POST['precio']
        stock_actual=request.POST['stock_actual'] #este nombre corresponde al del html
        proveedor_id=request.POST['proveedor']
        
       
        producto.nombre=nombre
        producto.precio=precio
        producto.stock_actual=stock_actual
        producto.proveedor_id=proveedor_id
        producto.save()
        

    return render(request,"modificar_producto.html",context)

def modificar_proveedor(request, proveedor_id):

    
    proveedor=Proveedor.objects.get(id=proveedor_id)
    

    context={
        "proveedor":proveedor,
        

    }


    if request.POST:
        nombre=request.POST['nombre']
        apellido=request.POST['apellido']
        dni=request.POST['dni'] #este nombre corresponde al del html
        
        
       
        proveedor.nombre=nombre
        proveedor.apellido=apellido
        proveedor.dni=dni
        #proveedor.proveedor_id=proveedor_id
        proveedor.save()
        

    return render(request,"modificar_proveedor.html",context)