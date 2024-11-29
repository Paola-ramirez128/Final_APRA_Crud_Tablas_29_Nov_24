from django.shortcuts import render, redirect
from .models import Empleado
# Create your views here.
def inicio_vistaEmpleados(request):
    losempleados = Empleado.objects.all()
    return render(request, "gestionarEmpleado.html", {"misempleados": losempleados})

def registrarEmpleado(request):
    id_empleado = request.POST['numid_empleado']
    direccion = request.POST['txtdireccion']
    telefono = request.POST['numtelefono']
    correo = request.POST['txtcorreo']
    sueldo = request.POST['numsueldo']
    horario = request.POST['txthorario']
    puesto = request.POST['txtpuesto']
    
    guardarEmpleado = Empleado.objects.create(
        id_empleado=id_empleado,direccion=direccion,telefono=telefono,correo=correo,
        sueldo=sueldo,horario=horario,puesto=puesto
    )

    return redirect("empleado")

def seleccionarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    return render(request, "editarempleado.html", {"misempleados": empleado})

def editarEmpleado(request):
    id_empleado = request.POST['numid_empleado']
    direccion = request.POST['txtdireccion']
    telefono = request.POST['numtelefono']
    correo = request.POST['txtcorreo']
    sueldo = request.POST['numsueldo']
    horario = request.POST['txthorario']
    puesto = request.POST['txtpuesto']
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.direccion = direccion
    empleado.telefono = telefono
    empleado.correo = correo
    empleado.sueldo = sueldo
    empleado.horario = horario
    empleado.puesto = puesto
    empleado.save()
    return redirect("empleado")

def borrarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("empleado")