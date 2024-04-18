from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from ips.models import Ip
from clientes.models import Cliente

def nuevo_ip(request):
    if request.method == 'POST':
        if request.POST.get('num'):
            ip = Ip()
            ip.num = request.POST.get('num')
            ip.usedby = request.POST.get('cliente')
            
            ip, created = Ip.objects.get_or_create(num=ip.num)
            
            if created:
                ip.usedby = request.POST.get('cliente')
                ip.save()
                return redirect('listado_ips')
            else:
                return HttpResponse('La IP ya existe')
    else:
        return render(request, 'ips/nuevo_ip.html')

def listado_ips(request):
    ips = Ip.objects.all()
    datos = {'ip': ips}
    return render(request, 'ips/listado_ips.html', datos)

def ip(request, ip_id):
    clientes = Cliente.objects.all()
    ip = Ip.objects.get(pk=ip_id)
    datos = {'ip': ip,
             'clientes': clientes}
    return render(request, 'ips/ip_detail.html', datos)

def eliminar_ip(request, ip_id):
    ip = Ip.objects.get(pk=ip_id)
    if request.method == 'POST':
        ip.delete()
        return redirect('listado_ips')
    else:
        return render(request, 'ips/eliminar_ip.html', {'ip': ip})
    
def asignar_ip(request, ip_id):
    
    ip = Ip.objects.get(pk=ip_id)
    
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        cliente = Cliente.objects.get(pk=cliente_id)
        ip.usedby = cliente
        cliente.ip_activo = Ip.objects.get(num=ip.num)
        ip.activo = True
        ip.save()
        return redirect('listado_ips')
    else:
        return redirect('asignar_ip', ip_id=ip.id)

def reset_ip(request, ip_id):
    ip = Ip.objects.get(pk=ip_id)
    if request.method == 'POST':
        ip.usedby = None
        ip.activo = False
        ip.save()
        return redirect('listado_ips')
    else:
        return render(request, 'ips/reset_ip.html', {'ip': ip})