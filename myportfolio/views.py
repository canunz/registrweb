import qrcode
from io import BytesIO
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento

# Vista principal
def index(request):
    return render(request, 'index.html')

# Vista para el formulario de evento
def evento(request):
    if request.method == "POST":
        nombre_evento = request.POST.get("nombre_evento")
        tipo_evento = request.POST.get("tipo_evento")
        
        # URL a codificar en el QR
        data = "https://docs.google.com/forms/d/e/1FAIpQLSd9tvN0cObQOOxErUnM4mEkgM7lZ-rSioOc_u9GERgnS7S3BQ/viewform?usp=sharing"
        
        # Generar el código QR
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill='black', back_color='white')
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        import base64
        img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

        context = {
            'qr_code_url': img_str
        }

        return render(request, 'evento.html', context)

    return render(request, 'evento.html')

# Vista para el registro de un evento
def registro(request, nombre_evento, tipo_evento):
    context = {
        'nombre_evento': nombre_evento,
        'tipo_evento': tipo_evento
    }
    return render(request, 'registro.html', context)

# Vista de login para el administrador
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Autenticación del usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige al dashboard si el login es exitoso
        else:
            # Agregar mensaje de error en caso de login fallido
            error_message = "Credenciales incorrectas"
            return render(request, 'admin_login.html', {'error_message': error_message})
    
    return render(request, 'admin_login.html')

# Vista para repartir los índices del evento
def reparto_indices(request):
    return render(request, 'reparto_indices.html')

# Vista protegida por login para el dashboard
@login_required
def dashboard(request):
    # Ejemplo de datos para el gráfico
    # Puedes obtener estos datos de la base de datos o cualquier otra fuente
    labels = ['Evento 1', 'Evento 2', 'Evento 3']
    data = [50, 75, 100]

    context = {
        'labels': labels,
        'data': data
    }

    return render(request, 'dashboard.html', context)
def evento_view(request):
    return render(request, 'evento.html')  # Aquí debes renderizar la plantilla evento.html

def indice_view(request):
    return render(request, 'indice.html')  # Aquí debes renderizar la plantilla indice.html

def evento_view(request):
    eventos = [
        {"id": 1, "nombre": "Evento A", "fecha": "2024-11-10", "participantes": 50, "asistentes": 30},
        {"id": 2, "nombre": "Evento B", "fecha": "2024-11-15", "participantes": 30, "asistentes": 15},
        {"id": 3, "nombre": "Evento C", "fecha": "2024-11-20", "participantes": 75, "asistentes": 55},
    ]
    return render(request, 'evento.html', {'eventos': eventos})

def modificar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    # Aquí puedes agregar lógica para modificar el evento
    return render(request, 'modificar_evento.html', {'evento': evento})

def eliminar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    evento.delete()
    return redirect('home') 

def registro_asistencia(request):
    if request.method == 'POST':
        nombre_completo = request.POST.get('nombre_completo')
        nuevo_asistente = Asistente(nombre=nombre_completo)
        nuevo_asistente.save()
        return redirect('registro_exitoso')
    return render(request, 'registro.html')

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')