from multiprocessing import context
from statistics import correlation
from django.shortcuts import render,redirect
from Citas.models import Clientes,Citas


# Create your views here.


def crearCita(request):    
    nombreCliente=request.POST['nombre']
    documentoCliente=request.POST['documento']
    sexoCliente=request.POST['sexo']
    telefonoCliente=request.POST['telefono']
    direccionCliente=request.POST['direccion']
    correoCliente=request.POST['correo']
    fechaNacimientoCliente=request.POST['fechaNacimiento']
    estadoCivilCliente=request.POST['estadoCivil']
    numeroHijosCliente=request.POST['numeroHijos']
    clientes=Clientes(nombre=nombreCliente,documento=documentoCliente,sexo=sexoCliente,telefono=telefonoCliente,direccion=direccionCliente,correo=correoCliente,fechaNacimiento=fechaNacimientoCliente,estadoCivil=estadoCivilCliente,numeroHijos=numeroHijosCliente)
    clientes.save()
    idCliente=clientes.idCliente    
    fechaCita=request.POST['fechaCita']
    servicioCita=request.POST['servicioCita']
    citas=Citas(fecha=fechaCita,servicio=servicioCita,idCliente_id=idCliente)
    citas.save()
    return redirect("/listarCita/")

def formularioCita(request):    
   
    return render(request,"crearCita.html")

def listarCita(request):   
    listarCita=Citas.objects.filter()
    listarClientes=Clientes.objects.filter()
    context={"crcita":listarCita,"lrClientes":listarClientes}

    return render(request,"Citas.html", context)

def editarCita(request, id):
    ver=Citas.objects.filter(idCitas=id).first()
    context={"ver":ver}
    return render(request,"editarCita.html",context)

def editarCliente(request, id):
    mostrar=Clientes.objects.filter(idCliente=id).first()    
    context={"mostrar":mostrar}
    return render(request,"editarCliente.html",context)

def actualizarCliente(request, id):
    nombreCliente=request.GET['nombre']
    documentoCliente=request.GET['documento']
    sexoCliente=request.GET['sexo']
    telefonoCliente=request.GET['telefono']
    direccionCliente=request.GET['direccion']
    correoCliente=request.GET['correo']
    fechaNacimientoCliente=request.GET['fechaNacimiento']
    estadoCivilCliente=request.GET['estadoCivil']
    numeroHijosCliente=request.GET['numeroHijos']
   
    actualizar=Clientes.objects.get(idCliente=id)
    actualizar.nombre=nombreCliente
    actualizar.sexo=sexoCliente
    actualizar.documento=documentoCliente
    actualizar.fechaNacimiento=fechaNacimientoCliente    
    actualizar.telefono=telefonoCliente
    actualizar.direccion=direccionCliente
    actualizar.correo=correoCliente    
    actualizar.estadoCivil=estadoCivilCliente
    actualizar.numeroHijos=numeroHijosCliente
    actualizar.save()

    return redirect("/listarCita/")
   
def actualizarCita(request, id):
    fechaCita=request.GET['fechaCita']
    servicioCita=request.GET['servicioCita']
    actualizar=Citas.objects.get(idCitas=id)
    actualizar.fecha=fechaCita
    actualizar.servicio=servicioCita
    actualizar.save()

    return redirect("/listarCita/")






