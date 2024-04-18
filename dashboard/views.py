from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from ips.models import Ip
from almacen.models import Articulo
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from clientes.models import Cliente
from brigadas.models import Brigada
from brigadas.models import articuloBrigada
from instalaciones.models import Instalacion
from almacen.models import Articulo
from soporte.models import Ticket
from movimientos.models import usoBrigada

user = get_user_model()

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")',
)

def login_page(request):
    return render(request, 'login.html')

@login_required(login_url='login_page')

def index(request):
    clientes_cant = Cliente.objects.all().count()
    articulos_cant = Articulo.objects.all().count()
    ips_cant = Ip.objects.all().count()
    brigadas_cant = Brigada.objects.all().count()
    pocos_articulos = Articulo.objects.filter(cantidad__lte=5)
    pc_brigada = articuloBrigada.objects.filter(cantidad__lte=5).order_by('brigada')
    tickets_cant = Ticket.objects.filter(solucionado=False).count()
    tickets_abiertos = Ticket.objects.filter(solucionado=False)[:10]
    instalaciones_pendientes = Instalacion.objects.filter(instalado=False)[:10]
    ult_movimientos = usoBrigada.objects.all().order_by('-fecha')[:10]
    
    datos = {
        'clientes_cant': clientes_cant,
        'articulos_cant': articulos_cant,
        'ips_cant': ips_cant,
        'brigadas_cant': brigadas_cant,
        'pocos_articulos': pocos_articulos,
        'pc_brigada': pc_brigada,
        'tickets_cant': tickets_cant,
        'tickets_abiertos': tickets_abiertos,
        'instalaciones': instalaciones_pendientes,
        'ult_movimientos': ult_movimientos
    }
    return render(request, 'index.html', datos)



def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('login_page')

def logout_page(request):
    return render(request, 'logout.html')

    


