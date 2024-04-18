from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cliente
from datetime import datetime
from datetime import datetime
from .models import Cliente
from instalaciones.models import Instalacion

def crear_cliente(request):
    if request.method == "POST":
        if request.POST.get('tipo') and request.POST.get('nombre') and request.POST.get('apellidos') and request.POST.get('email') and request.POST.get('telefono'):
            cliente = Cliente()
            cliente.nombre = request.POST.get('nombre')
            cliente.apellidos = request.POST.get('apellidos')
            cliente.cedula = request.POST.get('cedula')
            cliente.email = request.POST.get('email')
            cliente.telefono = request.POST.get('telefono')
            cliente.zona = request.POST.get('zona')
            cliente.direccion = request.POST.get('direccion')
            cliente.plan = request.POST.get('plan')
            if cliente.plan == 'fibra':
                cliente.mbps_f = request.POST.get('mbps_f')
                cliente.mbps_w = None
            else:
                cliente.mbps_w = request.POST.get('mbps_w')
                cliente.mbps_f = None
            cliente.subida = request.POST.get('subida')
            cliente.bajada = request.POST.get('bajada')
            cliente.f_nac = request.POST.get('f_nac')
            cliente.tipo = request.POST.get('tipo')
            cliente.f_reg = datetime.now()
            cliente.save()
            
            #nueva orden de instalacion
            instalacion = Instalacion() 
            instalacion.cliente = cliente
            instalacion.save()
            return redirect('listado')
        else:
            return render(request, "clientes/crear_cliente.html", {'error': 'Faltan datos'})
    else:
        return render(request, "clientes/crear_cliente.html") 


def editar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    datos = {'cliente': cliente}
    if request.method == 'POST':
        if request.POST.get('tipo'):
            cliente.nombre = request.POST.get('nombre')
            cliente.apellidos = request.POST.get('apellidos')
            cliente.cedula = request.POST.get('cedula')
            cliente.email = request.POST.get('email')
            cliente.telefono = request.POST.get('telefono')
            cliente.zona = request.POST.get('zona')
            cliente.direccion = request.POST.get('direccion')
            cliente.plan = cliente.plan
            cliente.mbps_f = request.POST.get('mbps_f')
            cliente.mbps_w = request.POST.get('mbps_w')
            if cliente.mbps_f != None:
                cliente.mbps_w = None  
            else:
                cliente.mbps_f = None
            cliente.subida = request.POST.get('subida')
            cliente.bajada = request.POST.get('bajada')

            cliente.save()
            return redirect('listado')
        else:
            return render(request, 'clientes/editar_cliente.html', datos)
    else:
        return render(request, 'clientes/editar_cliente.html', datos)

def cliente_detail(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})

def eliminar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listado')

def listado(request): 
    clientes = Cliente.objects.all()
    datos = { 'clientes': clientes }
    return render(request, 'clientes/listado.html', datos)
