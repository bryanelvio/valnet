from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from brigadas.models import Brigada, articuloBrigada
from instalaciones.models import Instalacion
from soporte.models import Ticket
from empleados.models import Empleados
from almacen.models import Articulo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from almacen.models import Articulo
from django.db.models import F
from equipos.models import Equipo



def listado_brigadas(request):
    brigadas = Brigada.objects.all()
    datos = {'brigadas': brigadas}
    return render(request, 'brigadas/listado_brigadas.html', datos)

def nueva_brigada(request):
    empleados = Empleados.objects.all()
    datos = {'empleados': empleados}
    
    if request.method == 'POST':
        if request.POST.get('placa') and request.POST.get('ficha') and request.POST.get('lider'):
            brigada = Brigada()
            brigada.placa = request.POST.get('placa')
            brigada.ficha = request.POST.get('ficha')
            brigada.lider = Empleados.objects.get(pk=request.POST.get('lider'))
            brigada.save()
            return redirect('listado_brigadas')
        else:
            return HttpResponse('falta un valor')
    else:
        return render(request, 'brigadas/nueva_brigada.html', datos)

def brigada(request, brigada_id):
    brigada = Brigada.objects.get(pk=brigada_id)
    equipos = Equipo.objects.filter(ubicacion=brigada.ficha)
    reportes = Ticket.objects.filter(brigada=brigada_id).order_by('solucionado')
    instalaciones = Instalacion.objects.filter(brigada=brigada_id).order_by('instalado')
    inventario = articuloBrigada.objects.filter(brigada=brigada_id).order_by('-fecha_ingreso')
    datos = {
        'brigada': brigada,
        'inventario': inventario,
        'equipos': equipos,
        'reportes': reportes,
        'instalaciones': instalaciones
        }
    
    return render(request, 'brigadas/brigada_detail.html', datos)


def transferir_articulo(request, brigada_id):
    almacen = Articulo.objects.all()
    articulo_brigada = articuloBrigada.objects.filter(brigada = brigada_id)
    brigada = Brigada.objects.get(pk=brigada_id)
    datos = {'brigada': brigada, 'almacen': almacen}
    
    if request.method == 'POST':
        if request.POST.get('nombre') and request.POST.get('cantidad'):
            articulo = Articulo.objects.get(pk=request.POST.get('nombre'))
            cantidad = int(request.POST.get('cantidad'))
            if cantidad > articulo.cantidad:
                return HttpResponse('No hay suficientes existencias disponibles.')
            elif cantidad <= 0:
                return HttpResponse('No se puede transferir una cantidad negativa o cero.')
            elif articulo_brigada.filter(articulo=articulo.nombre).exists():
                articulo_brigada.filter(articulo=articulo.nombre).update(
                    cantidad=F('cantidad') + cantidad
                    )
                brigada.save()
                articulo.cantidad -= cantidad
                articulo.save()
                return redirect('brigada', brigada_id)
            else:
                articuloBrigada.objects.create(
                    articulo=articulo.nombre, 
                    cantidad=cantidad,
                    medida=articulo.medida,
                    fecha_ingreso=timezone.now(),
                    brigada=brigada
                    )
                brigada.save()
                articulo.cantidad -= cantidad
                articulo.save()
                return redirect('brigada', brigada_id)
        else:
            return HttpResponse('falta un valor')
    else:
        return render(request, 'brigadas/transferir_articulo.html', datos)

def eliminar_articulo(request, articulo_id, brigada_id):
    
    articulo = articuloBrigada.objects.get(pk=articulo_id)
    articulo.delete()
    return redirect('brigada', brigada_id)

def eliminar_brigada(request, brigada_id):
    brigada = Brigada.objects.get(pk=brigada_id)
    if request.method == 'POST':
        brigada.delete()
        return redirect('listado_brigadas')
    else:
        return render(request, 'brigadas/eliminar_brigada.html', {'brigada': brigada})
    
def editar_brigada(request, brigada_id):
    brigada = Brigada.objects.get(pk=brigada_id)
    empleados = Empleados.objects.all()
    datos = {'brigada': brigada, 'empleados': empleados}
    
    if request.method == 'POST':
        if request.POST.get('placa') and request.POST.get('ficha') and request.POST.get('lider'):
            inventario = articuloBrigada()
            brigada.placa = request.POST.get('placa')
            brigada.ficha = request.POST.get('ficha')
            brigada.lider = Empleados.objects.get(pk=request.POST.get('lider'))
            inventario.objects.create(id = brigada_id)
            inventario.save()
            brigada.save()
            return redirect('listado_brigadas', datos)
        else:
            return HttpResponse('falta un valor')
    else:
        return render(request, 'brigadas/editar_brigada.html', datos)


def ordenes(request):
    brigadas = Brigada.objects.all()
    instalaciones = Instalacion.objects.filter(instalado = False).order_by('fecha')
    
    datos = {
        'instalaciones': instalaciones,
        'brigadas': brigadas
        }
    
    return render(request, 'brigadas/ordenes.html', datos)