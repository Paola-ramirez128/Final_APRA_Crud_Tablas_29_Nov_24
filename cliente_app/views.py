from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.
def inicio_vistaClientes(request):
    losclientes = Cliente.objects.all()
    return render(request, "gestionarCliente.html", {"misclientes":losclientes})

def registrarCliente(request):
    id_cliente = request.POST['numid_cliente']
    nombre = request.POST['txtnombre']
    telefono = request.POST['numtelefono']
    direccion = request.POST['txtdireccion']
    correo = request.POST['txtcorreo']
    pedidos = request.POST['numpedidos']
    fecha_registro = request.POST['txtfecha_registro']

    guardarCliente = Cliente.objects.create(
        id_cliente=id_cliente,nombre=nombre,telefono=telefono,direccion=direccion,
        correo=correo,pedidos=pedidos,fecha_registro=fecha_registro
    )
    return redirect("cliente")

def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    fecha_registro = cliente.fecha_registro.strftime('%Y-%m-%d')
    return render(request, "editarcliente.html", {"misclientes": cliente, "misclientes": cliente, "fecha_registro":fecha_registro})

def editarCliente(request):
    id_cliente = request.POST['numid_cliente']
    nombre = request.POST['txtnombre']
    telefono = request.POST['numtelefono']
    direccion = request.POST['txtdireccion']
    correo = request.POST['txtcorreo']
    pedidos = request.POST['numpedidos']
    fecha_registro = request.POST['txtfecha_registro']
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre = nombre
    cliente.telefono = telefono
    cliente.direccion = direccion
    cliente.correo = correo
    cliente.pedidos = pedidos
    cliente.fecha_registro = fecha_registro
    cliente.save()
    return redirect("cliente")

def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("cliente")