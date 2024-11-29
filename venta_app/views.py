from django.shortcuts import render, redirect
from .models import Venta
# Create your views here.
def inicio_vistaVentas(request):
    lasventas = Venta.objects.all()
    return render(request, "gestionarVenta.html", {"misventas":lasventas})

def registrarVenta(request):
    id_venta = request.POST['numid_venta']
    codigo_venta = request.POST['txtcodigo_venta']
    n_cliente = request.POST['numn_cliente']
    fecha_venta = request.POST['txtfecha_venta']
    precio = request.POST['numprecio']
    n_producto = request.POST['numn_producto']
    tipo_pago = request.POST['txttipo_pago']

    guardarVenta = Venta.objects.create(
        id_venta=id_venta,codigo_venta=codigo_venta,n_cliente=n_cliente,fecha_venta=fecha_venta,
        precio=precio,n_producto=n_producto,tipo_pago=tipo_pago
    )

    return redirect("venta")

def seleccionarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    fecha_venta = venta.fecha_venta.strftime('%Y-%m-%d')
    return render(request, "editarventa.html", {"misventas": venta, "misventas": venta, "fecha_venta": fecha_venta})

def editarVenta(request):
    id_venta = request.POST['numid_venta']
    codigo_venta = request.POST['txtcodigo_venta']
    n_cliente = request.POST['numn_cliente']
    fecha_venta = request.POST['txtfecha_venta']
    precio = request.POST['numprecio']
    n_producto = request.POST['numn_producto']
    tipo_pago = request.POST['txttipo_pago']
    venta = Venta.objects.get(id_venta=id_venta)
    venta.codigo_venta = codigo_venta
    venta.n_cliente = n_cliente
    venta.fecha_venta = fecha_venta
    venta.precio = precio
    venta.n_producto = n_producto
    venta.tipo_pago = tipo_pago
    venta.save()
    return redirect("venta")

def borrarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("venta")
