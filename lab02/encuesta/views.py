from django.shortcuts import render
from .forms import CalculadoraForm
from .forms import CilindroForm
from decimal import Decimal
import math
# Vista para mostrar el formulario
def index(request):
    context = {
        'titulo': "Formulario",
        
    }
    return render(request, 'encuesta/formulario.html', context)

# Vista para procesar los datos del formulario
def enviar (request):
    context = {
        'titulo': "Respuesta",
    'nombre': request. POST['nombre'],
    'clave': request. POST['password'],
    'educacion': request. POST['educacion'],
    'nacionalidad': request. POST['nacionalidad'],
    'idiomas': request.POST.getlist('idiomas'),
    'correo': request. POST['email'],
    'website': request.POST['sitioweb'],
    }
    return render (request, 'encuesta/respuesta.html', context)
def calcular(request):
    resultado = None

    if request.method == 'POST':
        form = CalculadoraForm(request.POST)
        if form.is_valid():
            numero1 = form.cleaned_data['numero1']
            numero2 = form.cleaned_data['numero2']
            operacion = form.cleaned_data['operacion']

            if operacion == 'suma':
                resultado = numero1 + numero2
            elif operacion == 'resta':
                resultado = numero1 - numero2
            elif operacion == 'multiplicacion':
                resultado = numero1 * numero2

    else:
        form = CalculadoraForm()

    return render(request, 'encuesta/calculadora.html', {'form': form, 'resultado': resultado})

def calcular_volumen(request):
    volumen = None

    if request.method == 'POST':
        form = CilindroForm(request.POST)
        if form.is_valid():
            altura = form.cleaned_data['altura']
            diametro = form.cleaned_data['diametro']

            # Convierte el diámetro en un Decimal
            diametro_decimal = Decimal(str(diametro))

            # Calcular el radio a partir del diámetro
            radio = diametro_decimal / Decimal('2.0')

            # Convierte math.pi en un Decimal
            pi = Decimal(str(math.pi))

            # Calcular el volumen del cilindro (π * r^2 * h)
            volumen = pi * radio ** 2 * altura

    else:
        form = CilindroForm()

    return render(request, 'encuesta/cilindro.html', {'form': form, 'volumen': volumen})