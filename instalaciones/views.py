from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from clientes.models import Cliente
from django.utils import timezone
from ips.models import Ip
from equipos.models import Equipo
from instalaciones.models import Instalacion
from soporte.models import Ticket
from brigadas.models import Brigada, articuloBrigada
from movimientos.models import usoBrigada

def instalaciones(request):
    instalaciones = Instalacion.objects.filter(instalado = False)
    clientes = Cliente.objects.filter(instalado = None)
    datos = { 
             'clientes': clientes,
             'instalaciones': instalaciones
             }
    return render(request, 'instalaciones/instalaciones.html', datos)

def instalacion(request, instalacion_id):

    instalacion = Instalacion.objects.get(pk=instalacion_id)
    brigadas = Brigada.objects.all()
    ips = Ip.objects.filter(usedby = None)
    equipos = Equipo.objects.filter(ubicacion = instalacion.brigada.ficha)
    
    materiales = articuloBrigada.objects.filter(brigada_id = instalacion.brigada.id)
    datos = {
        'instalacion': instalacion,
        'brigadas': brigadas,
        'ips': ips,
        'equipos': equipos,
        'materiales': materiales
        }
    
    if request.method == 'POST':
        if request.POST.get('ppp') and request.POST.get('c_nap') and request.POST.get('ip_activo') and request.POST.get('mac') and request.POST.get('emisor'):

            ## Sustraer materiales de inventario de brigada
            usados = []
            for articulo in materiales:
                if articulo.cantidad < int(request.POST.get('cantidad')):
                    return render(request, 'instalaciones/instalacion.html', datos, {
                        'error_cantidad': 'No hay suficientes materiales para realizar la instalación'
                        })
                else:
                    articulo.cantidad = articulo.cantidad - int(request.POST.get('cantidad'))
                    usados.append(articulo.articulo + ' ' + str(request.POST.get('cantidad')) + ' ' + articulo.medida)
                    articulo.save()

            
            nuevoUso = usoBrigada(
                    brigada = instalacion.brigada,
                    articulos_usados = usados,
                    cliente = instalacion.cliente,
                    )
            for articulo in usados:
                if request.POST.get('cantidad') == 0:
                    usados.remove(articulo) 
            nuevoUso.save()
            instalacion.instalado = True       
            instalacion.save()
            ## Actualizar Cliente
            instalacion.cliente.ppp = request.POST.get('ppp')
            instalacion.cliente.c_nap = request.POST.get('c_nap')
            instalacion.cliente.ip_activo = Ip.objects.get(pk = request.POST.get('ip_activo'))
            instalacion.cliente.mac = request.POST.get('mac')
            instalacion.cliente.emisor = request.POST.get('emisor')
            instalacion.cliente.instalado = timezone.now()
            instalacion.cliente.save()
            return redirect('instalaciones')
        else:
           return render(request, 'instalaciones/instalaciones.html', datos)
    else:
        return render(request, 'instalaciones/instalacion.html', datos)
    
        
