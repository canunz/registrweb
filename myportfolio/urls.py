from django.urls import path
from .views import index, evento, registro, admin_login, reparto_indices
from . import views

urlpatterns = [
    path('', index, name='home'),  # Vista principal
    path('evento/', evento, name='evento'),  # Vista de evento
    path('registro/<str:nombre_evento>/<str:tipo_evento>/', registro, name='registro'),  # Vista de registro
    path('admin_login/', admin_login, name='admin_login'),  # Vista de login para administrador
    path('reparto_indices/', reparto_indices, name='reparto_indices'),  # Vista de reparto e índices
    path('dashboard/', views.dashboard, name='dashboard'),  # Define la URL 'dashboard'
    path('evento/', views.evento_view, name='evento'),  # Ruta para el evento
    path('indice/', views.indice_view, name='indice'),  # Ruta para el índice
    path('evento/modificar/<int:id>/', views.modificar_evento, name='modificar_evento'),
    path('evento/eliminar/<int:id>/', views.eliminar_evento, name='eliminar_evento'),  # Vista para eliminar evento
    path('registro/', views.registro_asistencia, name='registro_asistencia'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
]

