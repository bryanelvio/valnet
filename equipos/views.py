from django.shortcuts import render
from equipos.models import Equipo
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from clientes.models import Cliente
from brigadas.models import Brigada

def nuevo_equipo(request):
    
    if request.method == 'POST':
        if request.POST.get('categoria') and request.POST.get('marca') and request.POST.get('modelo') and request.POST.get('serie'):
            equipo = Equipo()
            equipo.categoria = request.POST.get('categoria')
            equipo.marca = request.POST.get('marca')
            equipo.modelo = request.POST.get('modelo')
            equipo.mac = request.POST.get('mac')
            equipo.serie = request.POST.get('serie')
            equipo.pass_wifi = request.POST.get('pass_wifi')
            equipo.usuario = request.POST.get('usuario')
            equipo.clave = request.POST.get('clave')
            equipo.save()
            return redirect('equipos')
        else:
           return HttpResponse('algun valor invalido')
    else:
        return render(request, 'equipos/nuevo_equipo.html')
        
def listado_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/listado_equipos.html', {'equipos': equipos})

def editar_equipo(request, equipo_id):
    equipo = Equipo.objects.get(pk=equipo_id)
    brigadas = Brigada.objects.all()
    datos = {'equipo': equipo, 'brigadas': brigadas}
    if request.method == 'POST':
        if request.POST.get('categoria') and request.POST.get('marca') and request.POST.get('modelo') and request.POST.get('serie'):
            equipo.categoria = request.POST.get('categoria')
            equipo.marca = request.POST.get('marca')
            equipo.modelo = request.POST.get('modelo')
            equipo.mac = request.POST.get('mac')
            equipo.serie = request.POST.get('serie')
            equipo.pass_wifi = request.POST.get('pass_wifi')
            equipo.usuario = request.POST.get('usuario')
            equipo.clave = request.POST.get('clave')
            equipo.ubicacion = request.POST.get('ubicacion')
            equipo.save()
            return redirect('equipos')
        else:
           return render(request, 'equipos/editar_equipo.html', datos)
    else:
        return render(request, 'equipos/editar_equipo.html', datos)
   

def equipo_detail(request, equipo_id):
    clientes = Cliente.objects.all()
    brigadas = Brigada.objects.all()
    equipo = Equipo.objects.get(pk=equipo_id)
    return render(request, 'equipos/equipo_detail.html', {'equipo': equipo, 'brigadas': brigadas})

def eliminar_equipo(request, equipo_id):
    equipo = Equipo.objects.get(pk=equipo_id)
    equipo.delete()
    return redirect('equipos')

def asignar_equipo(request, equipo_id):
    equipo = Equipo.objects.get(pk=equipo_id)
    if request.method == 'POST':
        if request.POST.get('brigada'):
            equipo.ubicacion = request.POST.get('brigada')
            equipo.save()
            return redirect('equipos')
    else:
        return render(request, 'equipos/asignar_equipo.html', {'equipo': equipo})
    