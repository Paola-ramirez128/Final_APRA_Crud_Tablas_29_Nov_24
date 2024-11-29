from django.shortcuts import render, redirect
from .models import Producto

def inicio_vistaProductos(request):
    losproductos = Producto.objects.all()
    return render(request, "gestionarProducto.html", {"misproductos": losproductos})

def registrarProducto(request):
    id_producto = request.POST['numid_producto']
    precio = request.POST['numprecio']
    diseno = request.POST["txtdiseno"]
    fecha_entrega = request.POST['txtfecha_entrega']
    cantidad = request.POST['numcantidad']
    tamano = request.POST['txttamano']
    elaboracion_fecha = request.POST['txtelaboracion_fecha']

    guardarProducto = Producto.objects.create(
        id_producto=id_producto, precio=precio, diseno=diseno,
        fecha_entrega=fecha_entrega, cantidad=cantidad,tamano=tamano,
        elaboracion_fecha=elaboracion_fecha
    )

    return redirect("producto")

def seleccionarProducto(request, id_producto):  
    producto = Producto.objects.get(id_producto=id_producto) 
    fecha_entrega = producto.fecha_entrega.strftime('%Y-%m-%d') 
    return render(request, "editarproducto.html", {"misproductos": producto, "misproductos": producto, "fecha_entrega": fecha_entrega})

def editarProducto(request):  
    id_producto = request.POST['numid_producto']
    precio = request.POST['numprecio']
    diseno = request.POST['txtdiseno']
    fecha_entrega = request.POST['txtfecha_entrega']
    cantidad = request.POST['numcantidad']
    tamano = request.POST['txttamano']
    producto = Producto.objects.get(id_producto=id_producto)
    producto.precio = precio
    producto.diseno = diseno
    producto.fecha_entrega = fecha_entrega
    producto.cantidad = cantidad
    producto.tamano = tamano
    producto.save()  # guardar registro actualizado
    return redirect("producto")

def borrarProducto(request, id_producto): 
    producto = Producto.objects.get(id_producto=id_producto)  
    producto.delete()
    return redirect("producto")
