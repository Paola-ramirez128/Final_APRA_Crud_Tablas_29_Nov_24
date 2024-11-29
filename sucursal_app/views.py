from django.shortcuts import render, redirect
from .models import Sucursal
# Create your views here.
def inicio_vistaSucursales(request):
    lassucursales = Sucursal.objects.all()
    return render(request, "gestionarSucursal.html", {"missucursales": lassucursales})

def registrarSucursal(request):
    id_sucursal = request.POST['numid_sucursal']
    direccion = request.POST['txtdireccion']
    ciudad = request.POST['txtciudad']
    nombre = request.POST['txtnombre']
    encargado = request.POST['txtencargado']
    horario = request.POST['txthorario']
    telefono = request.POST['numtelefono']

    guardarSucursal = Sucursal.objects.create(
        id_sucursal=id_sucursal,direccion=direccion,ciudad=ciudad,nombre=nombre,
        encargado=encargado,horario=horario,telefono=telefono
    )

    return redirect("sucursal")

def seleccionarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    return render(request, "editarsucursal.html", {"missucursales": sucursal})

def editarSucursal(request):
    id_sucursal = request.POST['numid_sucursal']
    direccion = request.POST['txtdireccion']
    ciudad = request.POST['txtciudad']
    nombre = request.POST['txtnombre']
    encargado = request.POST['txtencargado']
    horario = request.POST['txthorario']
    telefono = request.POST['numtelefono']
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.direccion = direccion
    sucursal.ciudad = ciudad
    sucursal.nombre = nombre
    sucursal.encargado = encargado
    sucursal.horario = horario
    sucursal.telefono = telefono
    sucursal.save()
    return redirect("sucursal")

def borrarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()
    return redirect("sucursal")