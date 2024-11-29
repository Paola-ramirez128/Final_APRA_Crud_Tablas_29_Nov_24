from django.shortcuts import render, redirect
from .models import Proveedor
# Create your views here.
def inicio_vistaProveedores(request):
    losproveedores = Proveedor.objects.all()
    return render(request, "gestionarProveedores.html", {"misproveedores": losproveedores})

def registrarProveedor(request):
    id_proveedor = request.POST['numid_proveedor']
    telefono = request.POST['numtelefono']
    gmail = request.POST['txtgmail']
    raiting = request.POST['numraiting']
    registro_fecha = request.POST['txtregistro_fecha']
    tipo = request.POST['txttipo']
    provincia = request.POST['txtprovincia']

    guardarProveedor = Proveedor.objects.create(
        id_proveedor=id_proveedor,telefono=telefono,gmail=gmail,raiting=raiting,
        registro_fecha=registro_fecha,tipo=tipo,provincia=provincia
    )

    return redirect("proveedor")

def seleccionarProveedor(request, id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    registro_fecha = proveedor.registro_fecha.strftime('%Y-%m-%d')
    return render(request, "editarproveedores.html", {"misproveedores": proveedor, "misproveedores": proveedor, "registro_fecha": registro_fecha})

def editarProveedor(request):
    id_proveedor = request.POST['numid_proveedor']
    telefono = request.POST['numtelefono']
    gmail = request.POST['txtgmail']
    raiting = request.POST['numraiting']
    registro_fecha = request.POST['txtregistro_fecha']
    tipo = request.POST['txttipo']
    provincia = request.POST['txtprovincia']
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.telefono = telefono
    proveedor.gmail = gmail
    proveedor.raiting = raiting
    proveedor.registro_fecha = registro_fecha
    proveedor.tipo = tipo
    proveedor.provincia = provincia
    proveedor.save()
    return redirect("proveedor")

def borrarProveedor(reques,id_proveedor):
    proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete()
    return redirect("proveedor")