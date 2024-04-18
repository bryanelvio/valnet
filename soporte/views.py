from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from soporte.models import Ticket
from clientes.models import Cliente
from brigadas.models import Brigada
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import F
from datetime import date, timedelta, datetime
from soporte.models import Ticket
from datetime import timedelta




def nuevo_ticket(request):
    
    clientes = Cliente.objects.all()
    
    
    if request.method == 'POST':
       if request.POST.get('cliente') and request.POST.get('titulo') and request.POST.get('descripcion'):
            
            ticket = Ticket()
            ticket.cliente = Cliente.objects.get(pk=request.POST.get('cliente'))
           
            ticket.titulo = request.POST.get('titulo')
            ticket.descripcion = request.POST.get('descripcion')
            ticket.prioridad = request.POST.get('prioridad')
            
            if ticket.cliente.tipo == 'Residencial':
                ticket.f_compromiso = date.today() + timedelta(days=3)
            elif ticket.cliente.tipo == 'Empresarial':
                ticket.f_compromiso = date.today() + timedelta(days=2)
            elif ticket.cliente.tipo == 'Institucional':
                ticket.f_compromiso = date.today() + timedelta(days=1)
            
            ticket.save()
            return redirect('reportes')
       else:
            return render(request, 'soporte/nuevo_ticket.html', {'error': 'Hubo algún error al crear el ticket...', 'clientes': clientes})
    else:
        return render(request, 'soporte/nuevo_ticket.html', {'clientes': clientes})
        
## Listado de tickets a soporte
    
def listado_tickets(request):
    tickets = Ticket.objects.all().order_by('f_compromiso')
    current_date = date.today()

    datos = {
        'tickets': tickets, 
        }
    return render(request, 'soporte/tickets.html', datos)

## Reportes a tecnicos 

def reportes(request):
    tickets = Ticket.objects.all().filter(solucionado = False).order_by('f_compromiso')
    current_date = date.today()
    
    datos = {
        'tickets': tickets,
        }
    return render(request, 'instalaciones/reportes.html', datos)

def reporte(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    cliente = Cliente.objects.get(pk=ticket.cliente.id)
    datos = {'ticket': ticket, 'cliente': cliente}
    return render(request, 'instalacion/reporte.html', datos)

## Detalle de ticket a soporte

def ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    cliente = Cliente.objects.get(pk=ticket.cliente.id)
    datos = {'ticket': ticket, 'cliente': cliente}
    return render(request, 'soporte/ticket_detail.html', datos)

def eliminar_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('listado_tickets')
    else:
        return render(request, 'tickets/eliminar_ticket.html', {'ticket': ticket})
    
def cerrar_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        ticket.solucionado = True
        ticket.solucion = request.POST.get('solucion')
        ticket.nota = request.POST.get('nota')
        ticket.save()
        return redirect('listado_tickets')
    else:
        return render(request, 'soporte/cerrar_ticket.html', {'ticket': ticket})