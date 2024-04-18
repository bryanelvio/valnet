from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Articulo
from brigadas.models import articuloBrigada, Brigada

## def registrar_uso_articulo(request, articulo_id, cantidad_utilizada):
##     articulo = get_object_or_404(Articulo, id=articulo_id)
## 
##     if cantidad_utilizada > articulo.cantidad:
##         return JsonResponse({'mensaje': 'No hay suficientes existencias disponibles.'}, status=400)
## 
##     # Registra el uso del artículo y actualiza el inventario
##     RegistroUso.objects.create(usuario=request.user, articulo=articulo, cantidad_utilizada=cantidad_utilizada)
##     articulo.cantidad -= cantidad_utilizada
##     articulo.save()
## 
##     return JsonResponse({'mensaje': 'Uso de artículo registrado con éxito.'})

def almacen(request):
    articulos = Articulo.objects.all()
    datos = {'articulos': articulos}
    return render(request, 'almacen/almacen.html', datos)

def nuevo_articulo(request):
    if request.method == 'POST':
       if request.POST.get('nombre') and request.POST.get('descripcion') and request.POST.get('cantidad') and request.POST.get('medida'):
            articulo = Articulo()
            articulo.nombre = request.POST.get('nombre')
            articulo.descripcion = request.POST.get('descripcion')
            articulo.cantidad = request.POST.get('cantidad')
            articulo.medida = request.POST.get('medida')
            articulo.save()
            return redirect('almacen')
       else:
            return render(request, 'almacen/nuevo_articulo.html', {'error': 'Hubo algún error al crear el articulo...'})
    else:
        return render(request, 'almacen/nuevo_articulo.html')

def articulo(request, articulo_id):
    articulo = Articulo.objects.get(pk=articulo_id)
    datos = {'articulo': articulo}
    return render(request, 'almacen/articulo_detail.html', datos)

def editar_articulo(request, articulo_id):
    articulo = Articulo.objects.get(pk=articulo_id)
    datos = {'articulo': articulo}
    if request.method == 'POST':
        if request.POST.get('nombre') and request.POST.get('descripcion') and request.POST.get('cantidad') and request.POST.get('medida'):
            articulo.nombre = request.POST.get('nombre')
            articulo.descripcion = request.POST.get('descripcion')
            articulo.cantidad = request.POST.get('cantidad')
            articulo.medida = request.POST.get('medida')
            articulo.save()
            return redirect('almacen')
        else:
            return render(request, 'almacen/editar_articulo.html', {'error': 'Hubo algún error al editar el articulo...'})
    else:
        return render(request, 'almacen/editar_articulo.html', datos)
    
def eliminar_articulo(request, articulo_id):
    articulo = Articulo.objects.get(pk=articulo_id)
    articulo.delete()
    return redirect('almacen')

##def registrar_ingreso_articulo(request, articulo_id, cantidad_ingresada):
##    articulo = get_object_or_404(Articulo, id=articulo_id)
##
##    # Registra el ingreso del artículo y actualiza el inventario
##    articulo.cantidad += cantidad_ingresada
##    articulo.save()
##
##    return JsonResponse({'mensaje': 'Ingreso de artículo registrado con éxito.'})

def transferir_articulo(item_id, quantity):
    item_a = get_object_or_404(Articulo, id=item_id, cantidad__gte=quantity)
    item_b = get_object_or_404(articuloBrigada, id=item_id, cantidad__gte=quantity)
    inventario = articuloBrigada.objects.all()
    
    
    for b in inventario:
        if item_a.nombre == b.articulo:
            item_a.cantidad -= quantity
            item_a.save()
            b.cantidad += quantity
            b.save()
            return JsonResponse({'mensaje': f'{quantity} items transferred from inventory A to inventory B.'})
    item_a.cantidad -= quantity
    item_a.save()
    item_b.cantidad += quantity
    item_b.save()
    return JsonResponse({'mensaje': f'{quantity} items transferred from inventory A to inventory B.'})
            
def transferir(request, item_id, quantity):
    if request.method == 'POST':
        if request.POST.get('a_transfer') and request.POST.get('cantidad'):
            
            inventario = articuloBrigada.objects.all()
            almacen = Articulo.objects.all()
            articulo_b = articuloBrigada()
            articulo_transfer = request.POST.get('a_transfer')
            articulo_a = Articulo.objects.filter(nombre=articulo_transfer).first()
            cantidad = request.POST.get('cantidad')
            check_articulo = articuloBrigada.objects.filter(articulo=articulo_transfer).exists()
            
            if cantidad == '':
                return render(request, 'brigadas/transferir_articulo.html', {'error': 'Hubo algún error al transferir el articulo...'})
            elif cantidad == '0':
                return render(request, 'brigadas/transferir_articulo.html', {'error': 'Hubo algún error al transferir el articulo...'})
            elif cantidad > articulo_a.cantidad:
                return render(request, 'brigadas/transferir_articulo.html', {'error': 'No hay suficientes para transferir desde almacen...'})
            elif cantidad < 0:
                return render(request, 'brigadas/transferir_articulo.html', {'error': 'No se puede transferir cantidades negativas...'})
            elif check_articulo == True:
                articulo_a.cantidad -= int(cantidad)
                articulo_a.save()
                articulo_b.cantidad += int(cantidad)
                articulo_b.save()
                return redirect('brigada_detail')            
            else:
                articulo_a.cantidad -= int(cantidad)
                articulo_a.save()
                articulo_b.articulo = articulo_transfer
            



def registrar_salida_articulo(request, articulo_id, cantidad_salida):
    articulo = get_object_or_404(Articulo, id=articulo_id)

    if cantidad_salida > articulo.cantidad:
        return JsonResponse({'mensaje': 'No hay suficientes existencias disponibles.'}, status=400)

    # Registra el ingreso del artículo y actualiza el inventario
    articulo.cantidad -= cantidad_salida
    articulo.save()

    return JsonResponse({'mensaje': 'Salida de artículo registrado con éxito.'})

