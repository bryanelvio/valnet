from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from brigadas.models import Brigada
from instalaciones.models import Instalacion
from soporte.models import Ticket
from clientes.models import Cliente

def instalacion_brigada(request, instalacion_id):
    brigadas = Brigada.objects.all()
    instalacion = Instalacion.objects.get(pk=instalacion_id)
    datos = {'brigadas': brigadas}
    
    if request.method == 'POST':
        if request.POST.get('brigada'):
            instalacion.brigada = Brigada.objects.get(id = request.POST.get('brigada'))
            instalacion.save()
            return redirect('tickets_pendientes')
        else:
            return render(request, 'coordinacion/instalacion_brigada.html', datos)
    else:
        return render(request, 'coordinacion/instalacion_brigada.html', datos)

def reporte_brigada(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    brigadas = Brigada.objects.all()
    datos = {'brigadas': brigadas}
    
    if request.method == 'POST':
        if request.POST.get('brigada'):
            ticket.brigada = Brigada.objects.get(id = request.POST.get('brigada'))
            ticket.save()
            return redirect('tickets_pendientes')
        else:
            return render(request, 'coordinacion/reporte_brigada.html', datos)
    else:
        return render(request, 'coordinacion/reporte_brigada.html', datos)

def tickets_pendientes(request):
    tickets = Ticket.objects.filter(solucionado = False).order_by('f_compromiso')
    instalaciones = Instalacion.objects.filter(instalado = False).order_by('fecha')
    clientes_sin_instalar = Cliente.objects.filter(instalado = None)
    
    datos = {
        'tickets': tickets,
        'instalaciones': instalaciones,
        'clientes': clientes_sin_instalar
        }
    
    return render(request, 'coordinacion/tickets_pendientes.html', datos)


def tickets_cerrados(request):
    tickets = Ticket.objects.filter(solucionado = True).order_by('f_compromiso')
    instalaciones = Instalacion.objects.filter(instalado = True).order_by('fecha')
    
    datos = {
        'tickets': tickets,
        'instalaciones': instalaciones
        }

    return render(request, 'coordinacion/tickets_cerrados.html', datos)

    
    