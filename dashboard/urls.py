from django.urls import path
from django.conf.urls import include
from django import views
from dashboard import views
from clientes import views as clientes
from empleados import views as empleados
from instalaciones import views as instalaciones
from soporte import views as tickets
from ips import views as ips
from equipos import views as equipos
from almacen import views as almacen
from brigadas import views as brigadas

from coordinacion import views as coordinacion

urlpatterns = [
    ## Vistas principales
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('logout_page', views.logout_page, name='logout_page'),
    path('login_page', views.login_page, name='login_page'),
    
    ## Vistas Brigadas
    path('listado_brigadas/', brigadas.listado_brigadas, name='listado_brigadas'),
    path('nueva_brigada/', brigadas.nueva_brigada, name='nueva_brigada'),
    path('brigada/<int:brigada_id>', brigadas.brigada, name='brigada'),
    path('brigada/<int:brigada_id>/eliminar', brigadas.eliminar_brigada, name='eliminar_brigada'),
    path('brigada/<int:brigada_id>/editar', brigadas.editar_brigada, name='editar_brigada'),
    path('brigada/<int:brigada_id>/transferir_articulo', brigadas.transferir_articulo, name='transferir_articulo'),
    path('brigada/<int:brigada_id>/eliminar_articulo/<int:articulo_id>/', brigadas.eliminar_articulo, name='eliminar_articulo'),
    path('brigada/ordenes/', brigadas.ordenes, name='ordenes'),
    
    ## Vistas Clientes
    path('crear_cliente/', clientes.crear_cliente, name='crear_cliente'),
    path('cliente/<int:cliente_id>', clientes.cliente_detail, name='cliente_detail'),
    path('cliente/editar/<int:cliente_id>', clientes.editar_cliente, name='editar_cliente'),
    path('cliente/<int:cliente_id>/eliminar', clientes.eliminar_cliente, name='eliminar_cliente'),
    path('listado/', clientes.listado, name='listado'),
    
    ## Vistas Empleados
    path('nuevo_empleado/', empleados.nuevo_empleado, name='nuevo_empleado'),
    path('listado_empleados/', empleados.listado_empleados, name='listado_empleados'),

       
    ## Vistas Instalaciones
    path('instalaciones/', instalaciones.instalaciones, name='instalaciones'),
    path('instalacion/<int:instalacion_id>', instalaciones.instalacion, name='instalacion'),
    path('reportes/', tickets.reportes, name='reportes'),
    path('reporte/<int:ticket_id>', tickets.reporte, name='reporte'),
    
    ## Vistas Almacen
    path('almacen/', almacen.almacen, name='almacen'),
    path('articulo/<int:articulo_id>', almacen.articulo, name='articulo'),
    path('nuevo_articulo/', almacen.nuevo_articulo, name='nuevo_articulo'),
    path('articulo/<int:articulo_id>/editar', almacen.editar_articulo, name='editar_articulo'),
    path('articulo/<int:articulo_id>/eliminar', almacen.eliminar_articulo, name='eliminar_articulo'),
    
    ## Vistas Equipos
    path('listado_equipos/', equipos.listado_equipos, name='equipos'),
    path('nuevo_equipo/', equipos.nuevo_equipo, name='nuevo_equipo'),
    path('equipo/<int:equipo_id>', equipos.equipo_detail, name='equipo_detail'),
    path('equipo/<int:equipo_id>/editar', equipos.editar_equipo, name='equipo_editar'),
    path('equipo/<int:equipo_id>/eliminar', equipos.eliminar_equipo, name='eliminar_equipo'),
    
        
    #Vistas Tickets
    path('nuevo_ticket/', tickets.nuevo_ticket, name='nuevo_ticket'),
    path('tickets/', tickets.listado_tickets, name='tickets'),
    path('ticket/<int:ticket_id>', tickets.ticket, name='ticket'),
    path('ticket/<int:ticket_id>/eliminar', tickets.eliminar_ticket, name='eliminar_ticket'),
    
    #Vistas Coordinacion
    path('instalacion_brigada/<int:instalacion_id>', coordinacion.instalacion_brigada, name='instalacion_brigada'),
    path('reporte_brigada/<int:ticket_id>', coordinacion.reporte_brigada, name='reporte_brigada'),
    path('tickets_pendientes/', coordinacion.tickets_pendientes, name='tickets_pendientes'),
    path('tickets_cerrados/', coordinacion.tickets_cerrados, name='tickets_cerrados'),
    
    #Vistas Ips
    path('nuevo_ip/', ips.nuevo_ip, name='nuevo_ip'),
    path('listado_ips/', ips.listado_ips, name='listado_ips'),
    path('ip/<int:ip_id>', ips.ip, name='ip'),
    path('ip/<int:ip_id>/eliminar', ips.eliminar_ip, name='eliminar_ip'),
    path('ip/<int:ip_id>/asignar_ip', ips.asignar_ip, name='asignar_ip'),
    path('ip/<int:ip_id>/asignar', ips.asignar_ip, name='asignar_ip'),
    
    
]
