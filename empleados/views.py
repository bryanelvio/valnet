from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from empleados.models import Empleados as Empleado
from django.contrib.auth import get_user_model, login, logout

empleado = get_user_model()

def nuevo_empleado(request):
    departamentos = Group.objects.all()
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password1') and request.POST.get('password2') and request.POST.get('email') and request.POST.get('departamento'):
            if request.POST.get('password1') == request.POST.get('password2'):
                try:
                    empleado = Empleado.objects.create_user(
                        user=request.POST.get('username'), 
                        email=request.POST.get('email'), 
                        password=request.POST.get('password1'), 
                        departamento=request.POST.get('departamento'),
                    )
                    empleado.groups.add(request.POST.get('departamento'))
                    empleado.save()
                    return redirect('listado_empleados')
                except IntegrityError:
                    return render(request, 'empleados/crear_empleado.html', {'error': 'El nombre de empleado ya existe, favor elija uno nuevo.'}, {'departamentos': departamentos})
            else:
                # Add a message about mismatched passwords
                return render(request, 'empleados/crear_empleado.html', {'error': 'Las contraseñas no coinciden...'}, {'departamentos': departamentos})
        else:
            # Add a message about missing fields
            return render(request, 'empleados/crear_empleado.html', {'error': 'Falta un valor...'}, {'departamentos': departamentos})
    else:
        return render(request, 'empleados/crear_empleado.html', {'departamentos': departamentos})
            
def listado_empleados(request):
    empleados = Empleado.objects.all()
    datos = {'empleados': empleados}
    
    return render(request, 'empleados/listado_empleados.html', datos)

def editar_empleado(request, user_id):
    empleado = Empleado.objects.get(pk=user_id)
    datos = {'empleado': empleado}
    
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('email') and request.POST.get('departamento'):
            empleado.username = request.POST.get('username')
            empleado.email = request.POST.get('email')
            empleado.save()
            return redirect('listado_empleados')
        else:
            return HttpResponse('falta un valor')
    else:
        return render(request, 'empleados/editar_empleado.html', datos)

def editar_page_empleado(request, user_id):
    empleado = Empleado.objects.get(pk=user_id)
    return render(request, 'empleados/editar_page_user.html', {'empleado': empleado})

def usuario(request, user_id):
    user = User.objects.get(pk=user_id)
    datos = {'user': user}
    return render(request, 'empleados/usuario.html', datos)

def eliminar_empleado(request, user_id):
    empleado = Empleado.objects.get(pk=user_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('listado_empleados')